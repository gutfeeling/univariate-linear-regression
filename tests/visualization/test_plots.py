from math import cos, pi, sin

import pytest
import numpy as np

from visualization.plots import get_plot_for_best_fit_line


class TestGetPlotForBestFitLine(object):
    @pytest.mark.mpl_image_compare
    def test_plot_for_linear_data(self):
        slope = 2.0
        intercept = 1.0
        x_array = np.array([1.0, 2.0, 3.0])
        y_array = np.array([3.0, 5.0, 7.0])
        title = "Test plot for linear data"
        return get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title)

    @pytest.mark.mpl_image_compare
    def test_plot_for_circular_data(self):
        slope = 0.0
        intercept = 2.0
        theta = pi / 4.0
        x_array = np.array([2.0]) + np.array([cos(theta), cos(2 * theta), cos(3 * theta), cos(4 * theta), 
                                              cos(5 * theta), cos(6 * theta), cos(7 * theta), cos(8 * theta)
                                              ]
                                             )
        y_array = np.array([2.0]) + np.array([sin(theta), sin(2 * theta), sin(3 * theta), sin(4 * theta),
                                              sin(5 * theta), sin(6 * theta), sin(7 * theta), sin(8 * theta)
                                              ]
                                             )
        title = "Test plot for circular data"
        return get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title)

    def test_on_two_dimensional_x_array(self):
        slope = 2.0
        intercept = 1.0
        x_array = np.array([[1.0, 3.0], [2.0, 5.0]])
        y_array = np.array([3.0, 5.0])
        title = "Test on two dimensional x_array"
        with pytest.raises(ValueError) as exc_info:
            get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title)
        expected_error_msg = "Argument x_array should be 1 dimensional. It actually is 2 dimensional"
        exc_info.match(expected_error_msg)

    def test_on_two_dimensional_y_array(self):
        slope = 2.0
        intercept = 1.0
        x_array = np.array([1.0, 2.0])
        y_array = np.array([[1.0, 3.0], [2.0, 5.0]])
        title = "Test on two dimensional y_array"
        with pytest.raises(ValueError) as exc_info:
            get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title)
        expected_error_msg = "Argument y_array should be 1 dimensional. It actually is 2 dimensional"
        exc_info.match(expected_error_msg)

    def test_on_unequal_length_x_and_y_array(self):
        slope = 2.0
        intercept = 1.0
        x_array = np.array([1.0, 2.0])
        y_array = np.array([3.0, 5.0, 7.0])
        title = "Test on unequal length x and y array"
        with pytest.raises(RuntimeError) as exc_info:
            get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title)
        expected_error_msg = ("Arguments x_array and y_array should have same length. "
                              "But x_array has length 2 and y_array has length 3"
                              )
        exc_info.match(expected_error_msg)
