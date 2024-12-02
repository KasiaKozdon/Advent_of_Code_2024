import re
import unittest


def generate_answer(provided_data):
    left_input, right_input = separate_provided_data(provided_data)
    left_input = order(left_input)
    right_input = order(right_input)
    distance = calculate_distance(left_input, right_input)
    return sum_distances(distance)


def separate_provided_data(provided_data):
    provided_data = re.split("\n|\t|   ", provided_data.strip())
    provided_data = [int(i) for i in provided_data]
    left_input = provided_data[0::2]
    right_input = provided_data[1::2]
    return left_input, right_input


def order(input):
    input.sort()
    return input 


def calculate_distance(input1, input2):
    distance = [abs(input1[idx] - input2[idx] ) for idx, i in enumerate(input1)]
    return distance


def sum_distances(distances):
    return sum(distances)


def generate_answer_part2(provided_data):
    left_input, right_input = separate_provided_data(provided_data)
    distance = calculate_distance_part2(left_input, right_input)
    return sum_distances(distance)


def calculate_distance_part2(input1, input2):
    distance = [input1[idx] * calculate_occurences(input2, input1[idx]) for idx, i in enumerate(input1)]
    return distance


def calculate_occurences(sequence: list, item: int):
    return sequence.count(item)


class Test(unittest.TestCase):
    def test_with_provided_example(self):
        provided_data = ("3\t4\n"
                         "4\t3\n"
                         "2\t5\n"
                         "1\t3\n"
                         "3\t9\n"
                         "3\t3")

        predicted_answer = generate_answer(provided_data)
        expected_answer = 11
        self.assertEqual(expected_answer, predicted_answer)

    def test_with_provided_example_part2(self):
        provided_data = ("3\t4\n"
                         "4\t3\n"
                         "2\t5\n"
                         "1\t3\n"
                         "3\t9\n"
                         "3\t3")

        predicted_answer = generate_answer_part2(provided_data)
        expected_answer = 31
        self.assertEqual(expected_answer, predicted_answer)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=3, exit=False)

    with open("inputs/input1.txt") as f:
        data = f.read()

    # Part 1
    answer = generate_answer(data)
    print(f"Answer: {answer}")

    # Part 2
    answer = generate_answer_part2(data)
    print(f"Answer: {answer}")
