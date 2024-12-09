import os 
import re
import unittest

import numpy as np
import numpy.typing as npt

def generate_answer(input: str) -> int:
    # convert input to numpy
    width = input.find("\n") 
    height = input.count("\n") 
    input_as_np = np.empty((height, width), dtype=str)
    input = input.split("\n")
    for row_idx, row in enumerate(input):
        for letter_idx, letter in enumerate(row):
            input_as_np[row_idx, letter_idx] = letter

    # generate all strings
    possible_strings = []
    # horizontal
    possible_strings = list(np.apply_along_axis(convert_numpy_array_to_string, arr=input_as_np, axis=1))
    #possible_strings.append(input.split("\n"))
    # horizontal backwards
    possible_strings.extend([reverse_string(string) for string in possible_strings])
    # vertical up down
    possible_strings.extend(list(np.apply_along_axis(convert_numpy_array_to_string, arr=input_as_np, axis=0)))
    # vertical down up
    possible_strings.extend([reverse_string(string) for string in possible_strings[-height:]])
   
    #diagonal left top bottom
    possible_strings.extend([convert_numpy_array_to_string(np.diagonal(input_as_np, offset=j, axis1=0, axis2=1)) for j in range(-width, width)])
    #diagonal left bottom top
    possible_strings.extend([convert_numpy_array_to_string(np.diagonal(input_as_np, offset=j, axis1=1, axis2=0)) for j in range(-width, width)])
    #diagonal right top bottom
    possible_strings.extend([convert_numpy_array_to_string(np.fliplr(input_as_np).diagonal(offset=j, axis1=0, axis2=1)) for j in range(-width, width)])  # horizontal flip
    #diagonal right bottom top
    possible_strings.extend([convert_numpy_array_to_string(np.flipud(input_as_np).diagonal(offset=j, axis1=0, axis2=1)) for j in range(-width, width)])  # vertical flip

    xmas_instances = find_all_xmas(possible_strings)
    return xmas_instances


def convert_numpy_array_to_string(array: npt.ArrayLike) -> str:
    return ''.join(array.tolist())


def reverse_string(str_to_reverse: str) -> str:
    return str_to_reverse[::-1]


def find_all_xmas(possible_strings: list[str]) -> int:
    xmas_instances = 0
    for line in possible_strings:
        hits = re.findall("XMAS", line)
        xmas_instances += len(hits)
    return xmas_instances


class Test(unittest.TestCase):
    def test_with_provided_example(self):
        with open("inputs/input4_test.txt") as f:
            data = f.read()
        predicted_answer = generate_answer(data)
        expected_anser = 18
        self.assertEqual(expected_anser, predicted_answer)


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=3, exit=False)

    with open("inputs/input4.txt") as f:
        data = f.read()

    # Part 1
    answer = generate_answer(data)
    print(f"Answer: {answer}")


