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
    def test_plot_for_almost_linear_data(self):
        slope = -2.0
        intercept = 10.0
        x_array = np.array([1.0, 2.0, 3.0])
        y_array = np.array([8.0, 6.0, 5.0])
        title = "Test plot for almost linear data"
        return get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title)

