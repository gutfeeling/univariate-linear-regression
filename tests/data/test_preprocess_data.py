import pytest

from data.preprocess_data import preprocess


@pytest.fixture
def input_and_output_file(tmpdir):
    input_file_path = tmpdir.join("input_file.txt")
    with open(input_file_path, "w") as f:
        f.write("1,801\t201,411\n"
                "1,767565,112\n"
                "2,002\t333,209\n"
                "1990\t782,911\n"
                "1,285\t389129\n"
                )
    output_file_path = tmpdir.join("output_file.txt")
    return input_file_path, output_file_path


class TestPreprocess(object):
    def test_on_raw_data(self, input_and_output_file):
        input_file_path, output_file_path = input_and_output_file
        preprocess(input_file_path, output_file_path)
        with open(output_file_path, "r") as f:
            lines = f.readlines()
        num_lines = len(lines)
        assert num_lines == 2, "Output file should have 2 lines, it actually has {0} lines".format(num_lines)
        first_line = lines[0]
        assert first_line == "1801\t201411\n", "Expected: '1801\\t201411\\n', Actual: {0}".format(repr(first_line))
        second_line = lines[1]
        assert second_line == "2002\t333209\n", "Expected: '2002\\t333209\\n', Actual: {0}".format(repr(second_line))
