import numpy as np
import os

import pytest

from features.as_numpy import get_data_as_numpy_array


@pytest.fixture
def clean_data_file_path():
    file_path = "clean.txt"
    with open(file_path, "w") as f:
        f.write("201\t305671\n"
                "7892\t298140\n"
                "501\t738293\n"
                )
    yield file_path
    os.remove(file_path)


@pytest.fixture
def dirty_data_file_path():
    file_path = "dirty_data_file.txt"
    with open(file_path, "w") as f:
        f.write("201\t305671\n"
                "7892\t298140\n"
                "501\tbad_value\n"
                )
    yield file_path
    os.remove(file_path)


@pytest.fixture
def empty_file():
    file_path = "empty.txt"
    open(file_path, "w").close()
    yield file_path
    os.remove(file_path)


class TestGetDataAsNumpyArray(object):
    def test_on_clean_file(self, clean_data_file_path):
        expected = np.array([[201.0, 305671.0], [7892.0, 298140.0], [501.0, 738293.0]])
        actual = get_data_as_numpy_array(clean_data_file_path, 2)
        message = ("get_data_as_numpy_array({0}) should return {1}, "
                   "but it actually returned {2}".format(clean_data_file_path, expected, actual)
                   )
        assert actual == pytest.approx(expected), message

    def test_on_empty_file(self, empty_file):
        expected = np.empty((0, 2))
        actual = get_data_as_numpy_array(empty_file, 2)
        message = ("get_data_as_numpy_array({0}) should return {1}, "
                   "but it actually returned {2}".format(clean_data_file_path, expected, actual)
                   )
        assert actual == pytest.approx(expected), message

    def test_with_wrong_num_columns(self, clean_data_file_path):
        num_columns = 3
        with pytest.raises(ValueError) as exc_info:
            get_data_as_numpy_array(clean_data_file_path, num_columns)
        expected_error_msg = "Line 1 of {0} does not have {1} columns".format(clean_data_file_path, num_columns)
        assert exc_info.match(expected_error_msg)

    def test_with_non_float_value(self, dirty_data_file_path):
        with pytest.raises(ValueError) as exc_info:
            get_data_as_numpy_array(dirty_data_file_path, 2)
        expected_error_msg = "Line 3 of {0} is badly formatted".format(dirty_data_file_path)
        assert exc_info.match(expected_error_msg)
