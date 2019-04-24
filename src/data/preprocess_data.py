import argparse

from .preprocessing_helpers import row_to_list, convert_to_int


def preprocess(input_file_path, output_file_path):
    with open(input_file_path, "r") as input_file:
        rows = input_file.readlines()
    with open(output_file_path, "w") as output_file:
        for row in rows:
            row_as_list = row_to_list(row)
            if row_as_list is None:
                continue
            try:
                area = convert_to_int(row_as_list[0])
            except ValueError:
                continue
            try:
                price = convert_to_int(row_as_list[1])
            except ValueError:
                continue
            if area is None or price is None:
                continue
            output_file.write("{0}\t{1}\n".format(area, price))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file-path", "-i", type=str)
    parser.add_argument("--output-file-path", "-o", type=str)
    args = parser.parse_args()
    preprocess(**vars(args))
