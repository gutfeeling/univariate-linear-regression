import numpy as np
import pytest

from src import split_into_training_and_testing_sets


class TestSplitIntoTrainingAndTestingSets(object):
    def test_on_six_rows(self):
        test_input = np.array([[2081.0, 314942.0],
                               [1059.0, 186606.0],
                               [1148.0, 206186.0],
                               [1506.0, 248419.0],
                               [1210.0, 214114.0],
                               [1697.0, 277794.0],
                               ]
                              )
        actual = split_into_training_and_testing_sets(test_input)
        expected_length_training_set = 4
        expected_length_testing_set = 2
        actual_length_training_set = actual[0].shape[0]
        actual_length_testing_set = actual[1].shape[0]
        message_training_set = ("split_into_training_and_testing_set({0}) should return a training set of length {1}, "
                                "but it returned a training set of length {2}".format(test_input,
                                                                                      expected_length_training_set,
                                                                                      actual_length_training_set
                                                                                      )
                                )
        message_testing_set = ("split_into_training_and_testing_set({0}) should return a testing set of length {1}, "
                               "but it returned a testing set of length {2}".format(test_input,
                                                                                    expected_length_testing_set,
                                                                                    actual_length_testing_set
                                                                                    )
                               )
        assert actual_length_training_set == expected_length_training_set, message_training_set
        assert actual_length_testing_set == expected_length_testing_set, message_testing_set

    def test_on_eight_rows(self):
        test_input = np.array([[2081.0, 314942.0],
                               [1059.0, 186606.0],
                               [1148.0, 206186.0],
                               [1506.0, 248419.0],
                               [1210.0, 214114.0],
                               [1697.0, 277794.0],
                               [1382.0, 390167.0],
                               [8261.0, 911582.0],
                               ]
                              )
        actual = split_into_training_and_testing_sets(test_input)
        expected_length_training_set = 6
        expected_length_testing_set = 2
        actual_length_training_set = actual[0].shape[0]
        actual_length_testing_set = actual[1].shape[0]
        message_training_set = ("split_into_training_and_testing_set({0}) should return a training set of length {1}, "
                                "but it returned a training set of length {2}".format(test_input,
                                                                                      expected_length_training_set,
                                                                                      actual_length_training_set
                                                                                      )
                                )
        message_testing_set = ("split_into_training_and_testing_set({0}) should return a testing set of length {1}, "
                               "but it returned a testing set of length {2}".format(test_input,
                                                                                    expected_length_testing_set,
                                                                                    actual_length_testing_set
                                                                                    )
                               )
        assert actual_length_training_set == expected_length_training_set, message_training_set
        assert actual_length_testing_set == expected_length_testing_set, message_testing_set

    def test_on_two_rows(self):
        test_input = np.array([[1382.0, 390167.0],
                               [8261.0, 911582.0],
                               ]
                              )
        actual = split_into_training_and_testing_sets(test_input)
        expected_length_training_set = 1
        expected_length_testing_set = 1
        actual_length_training_set = actual[0].shape[0]
        actual_length_testing_set = actual[1].shape[0]
        message_training_set = ("split_into_training_and_testing_set({0}) should return a training set of length {1}, "
                                "but it returned a training set of length {2}".format(test_input,
                                                                                      expected_length_training_set,
                                                                                      actual_length_training_set
                                                                                      )
                                )
        message_testing_set = ("split_into_training_and_testing_set({0}) should return a testing set of length {1}, "
                               "but it returned a testing set of length {2}".format(test_input,
                                                                                    expected_length_testing_set,
                                                                                    actual_length_testing_set
                                                                                    )
                               )
        assert actual_length_training_set == expected_length_training_set, message_training_set
        assert actual_length_testing_set == expected_length_testing_set, message_testing_set

    def test_on_one_row(self):
        test_input = np.array([[1382.0, 390167.0]])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_input)
        expected_error_message_fragment = "Input data_array must have at least 2 rows, it actually has just 1"
        actual_error_message = str(exc_info)
        message = "Expected message fragment: {0}, Actual message: {1}".format(expected_error_message_fragment,
                                                                               actual_error_message
                                                                               )
        assert expected_error_message_fragment in actual_error_message, message

    def test_on_one_dimensional_array(self):
        test_input = np.array([1382.0, 390167.0])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_input)
        expected_error_message_fragment = "Input data_array must be two dimensional. Got 1 dimensional array instead!"
        actual_error_message = str(exc_info)
        message = "Expected message fragment: {0}, Actual message: {1}".format(expected_error_message_fragment,
                                                                               actual_error_message
                                                                               )
        assert expected_error_message_fragment in actual_error_message, message
