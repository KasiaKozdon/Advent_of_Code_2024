import os
import re
import unittest

def generate_answer(corrupted_instruction: str) -> int:
    instruction_result = 0
    valid_instruction = generate_valid_instruction(corrupted_instruction)
    for operation in valid_instruction:
        nums_to_multiply = identify_args(operation)
        instruction_result += nums_to_multiply[0] * nums_to_multiply[1]
    return instruction_result


def generate_answer_part_2(corrupted_instruction: str) -> int:
    inactive_instruction = r"don\'t\(\).*?do\(\)"
    corrupted_instruction = re.sub(inactive_instruction, "", corrupted_instruction)
    inactive_instruction_at_the_end = r"don\'t\(\).*"
    corrupted_instruction = re.sub(inactive_instruction_at_the_end, "", corrupted_instruction)
    return generate_answer(corrupted_instruction)


def generate_valid_instruction(corrupted_instruction: str) -> str:
    valid_instruction = re.findall(r"mul\(\d+,\d+\)", corrupted_instruction)
    return valid_instruction


def identify_args(operation: str) -> list[int]:
    operation_args = re.findall(r"\d+", operation)
    operation_args = [int(i) for i in operation_args]
    return operation_args


class Test(unittest.TestCase):
    def test_with_provided_example(self):
        provided_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        predicted_answer = generate_answer(provided_data)
        expected_answer = 161
        self.assertEqual(expected_answer, predicted_answer)


    def test_with_provided_example_part2(self):
        provided_data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        predicted_answer = generate_answer_part_2(provided_data)
        expected_answer = 48
        self.assertEqual(expected_answer, predicted_answer)


    def test_with_troubleshooting_example_part2(self):
        with open("inputs/input3_test.txt") as f:
            data = f.read().replace(os.linesep, "")
        predicted_answer = generate_answer_part_2(data)
        expected_answer = 2
        self.assertEqual(expected_answer, predicted_answer)

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=3, exit=False)

    with open("inputs/input3.txt") as f:
        data = f.read().replace(os.linesep, "")

    # Part 1
    answer = generate_answer(data)
    print(f"Answer: {answer}")

    # Part 2
    answer = generate_answer_part_2(data)
    print(f"Answer: {answer}")