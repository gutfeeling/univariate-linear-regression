from unittest.mock import call

import pytest

from data.preprocessing_helpers import convert_to_int, row_to_list, preprocess


@pytest.fixture
def input_and_output_file(tmpdir):
    input_file_path = tmpdir.join("input_file.txt")
    with open(input_file_path, "w") as f:
        f.write("1,801\t201,411\n"
                "1,767565,112\n"
                "2,002\t333,209\n"
                "1990\t782,911\n"
                "1,285\t389129\n"
                )
    output_file_path = tmpdir.join("output_file.txt")
    return input_file_path, output_file_path


def row_to_list_side_effect(row):
    return_values = {"1,801\t201,411\n": ["1,801", "201,411"],
                     "2,002\t333,209\n": ["2,002", "333,209"],
                     }
    if row in return_values:
        return return_values[row]
    return None


def convert_to_int_side_effect(comma_separated_integer_string):
    return_values = {"1,801": 1801,
                     "201,411": 201411,
                     "2,002": 2002,
                     "333,209": 333209,
                     }
    return return_values[comma_separated_integer_string]


class TestConvertToInt(object):
    def test_with_no_comma(self):
        test_argument = "756"
        expected = 756
        actual = convert_to_int(test_argument)
        assert actual == expected, "Expected: 756, Actual: {0}".format(actual)

    def test_with_one_comma(self):
        test_argument = "2,081"
        expected = 2081
        actual = convert_to_int(test_argument)
        assert actual == expected, "Expected: 2081, Actual: {0}".format(actual)

    def test_with_two_commas(self):
        test_argument = "1,034,891"
        expected = 1034891
        actual = convert_to_int(test_argument)
        assert actual == expected, "Expected: 1034891, Actual: {0}".format(actual)

    def test_on_string_with_incorrectly_placed_comma(self):
        test_argument = "12,72,891"
        expected = None
        actual = convert_to_int(test_argument)
        assert actual == expected, "Expected: None, Actual: {0}".format(actual)

    def test_on_string_with_missing_comma(self):
        test_argument = "178100,301"
        expected = None
        actual = convert_to_int(test_argument)
        assert actual == expected, "Expected: None, Actual: {0}".format(actual)

    def test_on_float_valued_string(self):
        test_argument = "6.9"
        expected = None
        actual = convert_to_int(test_argument)
        assert actual == expected, "Expected: None, Actual: {0}".format(actual)


class TestRowToList(object):
    def test_on_no_tab_no_missing_value(self):    # (0, 0) boundary value
        actual = row_to_list("123\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_two_tabs_no_missing_value(self):    # (2, 0) boundary value
        actual = row_to_list("123\t4,567\t89\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_one_tab_with_missing_value(self):    # (1, 1) boundary value
        actual = row_to_list("\t4,567\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_no_tab_with_missing_value(self):    # (0, 1) case
        actual = row_to_list("\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_two_tabs_with_missing_value(self):    # (0, 1) case
        actual = row_to_list("123\t\t89\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_normal_argument_1(self):
        actual = row_to_list("123\t4,567\n")
        expected = ["123", "4,567"]
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)

    def test_on_normal_argument_2(self):
        actual = row_to_list("1,059\t186,606\n")
        expected = ["1,059", "186,606"]
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)


class TestPreprocess(object):
    def test_on_raw_data(self, input_and_output_file, mocker):
        input_file_path, output_file_path = input_and_output_file
        row_to_list_mock = mocker.patch("data.preprocessing_helpers.row_to_list", side_effect=row_to_list_side_effect)
        convert_to_int_mock = mocker.patch("data.preprocessing_helpers.convert_to_int",
                                           side_effect=convert_to_int_side_effect
                                           )
        preprocess(input_file_path, output_file_path)
        assert row_to_list_mock.call_args_list == [call("1,801\t201,411\n"),
                                                   call("1,767565,112\n"),
                                                   call("2,002\t333,209\n"),
                                                   call("1990\t782,911\n"),
                                                   call("1,285\t389129\n")
                                                   ]
        assert convert_to_int_mock.call_args_list == [call("1,801"), call("201,411"), call("2,002"), call("333,209")]
        with open(output_file_path, "r") as f:
            lines = f.readlines()
        num_lines = len(lines)
        assert num_lines == 2, "Output file should have 2 lines, it actually has {0} lines".format(num_lines)
        first_line = lines[0]
        assert first_line == "1801\t201411\n", "Expected: '1801\\t201411\\n', Actual: {0}".format(repr(first_line))
        second_line = lines[1]
        assert second_line == "2002\t333209\n", "Expected: '2002\\t333209\\n', Actual: {0}".format(repr(second_line))


