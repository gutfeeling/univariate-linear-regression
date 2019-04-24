import sys

import pytest

from src import convert_to_int, row_to_list


@pytest.mark.skipif(sys.version_info < (3, 6), reason="Uses f-strings, only works for Python versions > 3.6")
class TestConvertToInt(object):
    def test_on_string_smaller_than_thousand(self):
        test_argument = "756"
        expected = 756
        actual = convert_to_int(test_argument)
        message = "convert_to_int({test_argument}) should return {expected}, but it actually returned {actual}"
        assert actual == expected, message

    def test_on_string_with_one_comma(self):
        test_argument = "2,081"
        expected = 2081
        actual = convert_to_int(test_argument)
        message = "convert_to_int({test_argument}) should return {expected}, but it actually returned {actual}"
        assert actual == expected, message

    def test_on_string_with_two_commas(self):
        test_argument = "1,034,891"
        expected = 1034891
        actual = convert_to_int(test_argument)
        message = "convert_to_int({test_argument}) should return {expected}, but it actually returned {actual}"
        assert actual == expected, message

    def test_on_string_with_incorrect_commas(self):
        test_argument = "12,72,891"
        expected = None
        actual = convert_to_int(test_argument)
        message = "convert_to_int({test_argument}) should return {expected}, but it actually returned {actual}"
        assert actual == expected, message

    def test_on_string_with_missing_comma(self):
        test_argument = "178100,301"
        expected = None
        actual = convert_to_int(test_argument)
        message = "convert_to_int({test_argument}) should return {expected}, but it actually returned {actual}"
        assert actual == expected, message

    def test_on_float_valued_string(self):
        test_argument = "23,816.92"
        expected = None
        actual = convert_to_int(test_argument)
        message = "convert_to_int({test_argument}) should return {expected}, but it actually returned {actual}"
        assert actual == expected, message


class TestRowToList(object):
    def test_on_clean_row_with_tab(self):
        test_argument = "2,081\t314,942\n"
        expected = ["2,081", "314,942"]
        actual = row_to_list(test_argument)
        message = "row_to_list({0}) should return {1}, but it actually returned {2}".format(repr(test_argument),
                                                                                            expected,
                                                                                            actual,
                                                                                            )
        assert actual == expected, message

    def test_on_clean_row_with_space(self):
        test_argument = "1,059 186,606\n"
        expected = ["1,059", "186,606"]
        actual = row_to_list(test_argument)
        message = "row_to_list({0}) should return {1}, but it actually returned {2}".format(repr(test_argument),
                                                                                            expected,
                                                                                            actual,
                                                                                            )
        assert actual == expected, message

    def test_on_row_with_one_value(self):
        test_argument = "\t293,410\n"
        expected = None
        actual = row_to_list(test_argument)
        message = "row_to_list({0}) should return {1}, but it actually returned {2}".format(repr(test_argument),
                                                                                            expected,
                                                                                            actual,
                                                                                            )
        assert actual == expected, message

    def test_on_row_with_three_values(self):
        test_argument = "301\t678,219\t56,720n"
        expected = None
        actual = row_to_list(test_argument)
        message = "row_to_list({0}) should return {1}, but it actually returned {2}".format(repr(test_argument),
                                                                                            expected,
                                                                                            actual,
                                                                                            )
        assert actual == expected, message

    def test_on_row_with_no_separator(self):
        test_argument = "1,463238,765\n"
        expected = None
        actual = row_to_list(test_argument)
        message = "row_to_list({0}) should return {1}, but it actually returned {2}".format(repr(test_argument),
                                                                                            expected,
                                                                                            actual,
                                                                                            )
        assert actual == expected, message

    def test_on_row_with_space_and_tab(self):
        test_argument = " 45,781\t293,410\n"
        expected = None
        actual = row_to_list(test_argument)
        message = "row_to_list({0}) should return {1}, but it actually returned {2}".format(repr(test_argument),
                                                                                            expected,
                                                                                            actual,
                                                                                            )
        assert actual == expected, message

    def test_on_row_with_tab_and_space(self):
        test_argument = "45,781\t293, 410\n"
        expected = None
        actual = row_to_list(test_argument)
        message = "row_to_list({0}) should return {1}, but it actually returned {2}".format(repr(test_argument),
                                                                                            expected,
                                                                                            actual,
                                                                                            )
        assert actual == expected, message


