import pytest

from data.preprocessing_helpers import convert_to_int, row_to_list


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


