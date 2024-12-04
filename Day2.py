from itertools import pairwise
import re
import unittest


def  generate_answer(provided_data, fault_tolerance=False) -> int:
    safe_reports = 0 
    provided_data = provided_data.strip().split('\n')
    for line in provided_data:
        line = line.split(' ')
        line = [int(i) for i in line]

        differences = calculate_differences(line)
        line_safe = check_if_monotonous(differences) and check_if_within_bounds(differences)
        if fault_tolerance and not line_safe:
            for idx in range(len(line)):
                partial_line = line.copy()
                partial_line.pop(idx)
                differences = calculate_differences(partial_line)
                line_safe = check_if_monotonous(differences) and check_if_within_bounds(differences)
                if line_safe:
                    break
        if line_safe:
            safe_reports += 1

    return safe_reports


def calculate_differences(input: list) -> list:
    return [a - b for a, b in pairwise(input)]

def check_if_monotonous(input: list) -> bool:
    "Requirement: The levels are either all increasing or all decreasing"
    are_monotonous = all(i > 0 for i in input) or all(i < 0 for i in input) 
    return are_monotonous


def check_if_within_bounds(input: list, lower_bound: int = 1, upper_bound: int = 3) -> bool:
    "Any two adjacent levels differ by at least one and at most three."
    are_within_bounds = all(abs(i) >= lower_bound for i in input) and all(abs(i) <= upper_bound for i in input) 
    return are_within_bounds

class Test(unittest.TestCase):
    def test_with_provided_example(self):
        provided_data = ("7 6 4 2 1\n"
                         "1 2 7 8 9\n"
                         "9 7 6 2 1\n"
                         "1 3 2 4 5\n"
                         "8 6 4 4 1\n"
                         "1 3 6 7 9")
        
        predicted_answer = generate_answer(provided_data)
        expected_answer = 2
        self.assertEqual(expected_answer, predicted_answer)


    def test_with_provided_example_part2(self):
        provided_data = ("7 6 4 2 1\n"
                         "1 2 7 8 9\n"
                         "9 7 6 2 1\n"
                         "1 3 2 4 5\n"
                         "8 6 4 4 1\n"
                         "1 3 6 7 9")
        
        predicted_answer = generate_answer(provided_data, fault_tolerance=True)
        expected_answer = 4
        self.assertEqual(expected_answer, predicted_answer)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=3, exit=False)

    with open("inputs/input2.txt") as f:
        data = f.read()

    # Part 1
    answer = generate_answer(data)
    print(f"Answer: {answer}")

    # Part 2
    answer = generate_answer(data, fault_tolerance=True)
    print(f"Answer: {answer}")