import numpy as np


def get_data_as_numpy_array(processed_data_file_path):
    data_array_one_dim = np.fromfile(processed_data_file_path, count=-1, sep="\t")
    data_array = data_array_one_dim.reshape(-1, 2)
    return data_array
