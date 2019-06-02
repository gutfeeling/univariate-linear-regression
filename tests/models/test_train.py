from math import cos, pi, sin
import numpy as np
import pytest

from models.train import split_into_training_and_testing_sets, train_model, model_test


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
        expected_length_training_set = 4
        expected_length_testing_set = 2
        actual = split_into_training_and_testing_sets(test_input)
        assert actual[0].shape[0] == expected_length_training_set, \
               "The actual number of rows in the training array is not 4"
        assert actual[1].shape[0] == expected_length_testing_set, \
               "The actual number of rows in the testing array is not 2"

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
        expected_length_training_set = 6
        expected_length_testing_set = 2
        actual = split_into_training_and_testing_sets(test_input)
        assert actual[0].shape[0] == expected_length_training_set, \
               "The actual number of rows in the training array is not 6"

        assert actual[1].shape[0] == expected_length_testing_set, \
               "The actual number of rows in the testing array is not 2"

    def test_on_two_rows(self):
        test_input = np.array([[1382.0, 390167.0],
                               [8261.0, 911582.0],
                               ]
                              )
        expected_length_training_set = 1
        expected_length_testing_set = 1
        actual = split_into_training_and_testing_sets(test_input)
        assert actual[0].shape[0] == expected_length_training_set, \
               "The actual number of rows in the training array is not 1"
        assert actual[1].shape[0] == expected_length_testing_set, \
               "The actual number of rows in the testing array is not 1"

    def test_on_one_row(self):
        test_argument = np.array([[1382.0, 390167.0]])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
        expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
        assert exc_info.match(expected_error_msg)

    def test_on_one_dimensional_array(self):
        test_input = np.array([1382.0, 390167.0])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_input)
        expected_error_msg = "Argument data_array must be two dimensional. Got 1 dimensional array instead!"
        assert exc_info.match(expected_error_msg)


class TestTrainModel(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected_slope = 2.0
        expected_intercept = 1.0
        actual_slope, actual_intercept = train_model(test_input)
        slope_message = ("train_model({0}) should return slope {1}, "
                         "but it actually returned slope {2}".format(test_input, expected_slope, actual_slope)
                         )
        intercept_message = ("train_model({0}) should return intercept {1}, "
                             "but it actually returned intercept {2}".format(test_input,
                                                                             expected_intercept,
                                                                             actual_intercept
                                                                             )
                             )
        assert actual_slope == pytest.approx(expected_slope), slope_message
        assert actual_intercept == pytest.approx(expected_intercept), intercept_message

    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            train_model(test_input)
        expected_error_message_fragment = ("The training_set input must be two dimensional. "
                                           "Got 1 dimensional array instead!"
                                           )
        actual_error_message = str(exc_info)
        message = "Expected message fragment: {0}, Actual message: {1}".format(expected_error_message_fragment,
                                                                               actual_error_message
                                                                               )
        assert expected_error_message_fragment in actual_error_message, message

    def test_on_one_row(self):
        test_input = np.array([[1382.0, 390167.0]])
        with pytest.raises(ValueError) as exc_info:
            train_model(test_input)
        expected_error_message_fragment = ("The training_set input must have at least 2 rows for linear regression "
                                           "to work, it actually has just 1"
                                           )
        actual_error_message = str(exc_info)
        message = "Expected message fragment: {0}, Actual message: {1}".format(expected_error_message_fragment,
                                                                               actual_error_message
                                                                               )
        assert expected_error_message_fragment in actual_error_message, message

    def test_on_three_columns(self):
        test_input = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        with pytest.raises(ValueError) as exc_info:
            train_model(test_input)
        expected_error_message_fragment = ("The training_set input must have 2 columns for univariate linear "
                                           "regression. It actually has 3 columns"
                                           )
        actual_error_message = str(exc_info)
        message = "Expected message fragment: {0}, Actual message: {1}".format(expected_error_message_fragment,
                                                                               actual_error_message
                                                                               )
        assert expected_error_message_fragment in actual_error_message, message


class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        message = "model_test({0}) should return {1}, but it actually returned {2}".format(test_input,
                                                                                           expected,
                                                                                           actual
                                                                                           )
        assert actual == pytest.approx(expected), message

    def test_on_circular_data(self):
        theta = pi/4.0
        test_input = np.array([[cos(theta), sin(theta)],
                               [cos(2 * theta), sin(2 * theta)],
                               [cos(3 * theta), sin(3 * theta)],
                               [cos(4 * theta), sin(4 * theta)],
                               [cos(5 * theta), sin(5 * theta)],
                               [cos(6 * theta), sin(6 * theta)],
                               [cos(7 * theta), sin(7 * theta)],
                               [cos(8 * theta), sin(8 * theta)],
                               ]
                              )
        actual = model_test(test_input, 0.0, 0.0)
        message = ("model_test() should return 0 on circular data with center at 0 and fitted line y = 0, "
                   "it actually returned {0}".format(actual)
                   )
        assert actual == pytest.approx(0.0), message

    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)
        expected_error_message_fragment = ("The testing_set input must be two dimensional. "
                                           "Got 1 dimensional array instead!"
                                           )
        actual_error_message = str(exc_info)
        message = "Expected message fragment: {0}, Actual message: {1}".format(expected_error_message_fragment,
                                                                               actual_error_message
                                                                               )
        assert expected_error_message_fragment in actual_error_message, message

    def test_on_three_columns(self):
        test_input = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)
        expected_error_message_fragment = ("The testing_set input must have 2 columns for univariate linear "
                                           "regression. It actually has 3 columns"
                                           )
        actual_error_message = str(exc_info)
        message = "Expected message fragment: {0}, Actual message: {1}".format(expected_error_message_fragment,
                                                                               actual_error_message
                                                                               )
        assert expected_error_message_fragment in actual_error_message, message


@pytest.mark.xfail(reason="get_correlation_coefficient() is not implemented yet")
class TestGetCorrelationCoefficient(object):
    def test_on_perfect_positive(self):
        test_input = np.array([[1.0, 3.0],
                               [2.0, 5.0],
                               [3.0, 7.0],
                               ]
                              )
        expected = 1.0
        actual = get_correlation_coefficient(test_input)
        message = "get_correlation_coefficient({0}) should return {1}, but it actually returned {2}".format(test_input,
                                                                                                            expected,
                                                                                                            actual
                                                                                                            )
        assert actual == pytest.approx(expected), message

    def test_on_perfect_negative(self):
        test_input = np.array([[1.0, -2.0],
                               [2.0, -5.0],
                               [3.0, -8.0],
                               ]
                              )
        expected = -1.0
        actual = get_correlation_coefficient(test_input)
        message = "get_correlation_coefficient({0}) should return {1}, but it actually returned {2}".format(test_input,
                                                                                                            expected,
                                                                                                            actual
                                                                                                            )
        assert actual == pytest.approx(expected), message

    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            get_correlation_coefficient(test_input)
        expected_error_message_fragment = ("The data input must be two dimensional. "
                                           "Got 1 dimensional array instead!"
                                           )
        actual_error_message = str(exc_info)
        message = "Expected message fragment: {0}, Actual message: {1}".format(expected_error_message_fragment,
                                                                               actual_error_message
                                                                               )
        assert expected_error_message_fragment in actual_error_message, message

    def test_on_three_columns(self):
        test_input = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        with pytest.raises(ValueError) as exc_info:
            get_correlation_coefficient(test_input)
        expected_error_message_fragment = ("The data input must have 2 columns for finding correlation "
                                           "coefficient. It actually has 3 columns"
                                           )
        actual_error_message = str(exc_info)
        message = "Expected message fragment: {0}, Actual message: {1}".format(expected_error_message_fragment,
                                                                               actual_error_message
                                                                               )
        assert expected_error_message_fragment in actual_error_message, message



