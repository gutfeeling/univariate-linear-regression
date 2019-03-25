import numpy as np
from scipy.stats import linregress


def split_into_training_and_training_sets(data_array):
    num_training = int(0.75 * data_array.shape[0])
    permuted_indices = np.random.permutation(data_array.shape[0])
    return data_array[permuted_indices[:num_training], :], data_array[permuted_indices[num_training:], :]


def test_model(testing_set, slope, intercept):
    actual_price = testing_set[:, 1]
    predicted_price = slope*testing_set[:, 0] + intercept
    return 1 - np.var(predicted_price - actual_price) / np.var(actual_price)


def train_model(training_set):
    slope, intercept, _, _, _ = linregress(training_set[:, 0], training_set[:, 1])
    return slope, intercept

