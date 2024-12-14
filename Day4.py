import unittest


def generate_answer(input: str) -> int:
    input = input.rstrip().split("\n")

    xmas_instances = 0
    for row_idx, row in enumerate(input):
        for letter_idx, letter in enumerate(row):
            if letter == "X":
                for x_stride in [-1, 0, 1]:
                    for y_stride in [-1, 0, 1]:
                            xmas_instances += find_xmas_string(input,
                            x_stride = x_stride, y_stride = y_stride, 
                            starting_x = letter_idx, starting_y = row_idx,
                            str_to_find = "XMAS")
                    
    return xmas_instances


def generate_answer_part2(input: str) -> int:
    input = input.rstrip().split("\n")

    x_mas_instances = 0
    for row_idx, row in enumerate(input):
        for letter_idx, _ in enumerate(row):
            # Find top left - bottom right half of the cross, either direction
            x_stride = 1
            y_stride = 1
            if find_xmas_string(input,
                        x_stride = x_stride, y_stride = y_stride, 
                        starting_x = letter_idx, starting_y = row_idx,
                        str_to_find = "MAS") or find_xmas_string(input,
                        x_stride = x_stride, y_stride = y_stride, 
                        starting_x = letter_idx, starting_y = row_idx,
                        str_to_find = "SAM"):
                # Find top righ - bottom left half of the cross, either direction
                x_stride = -1
                y_stride = 1
                starting_x = letter_idx + 2
                if find_xmas_string(input,
                            x_stride = x_stride, y_stride = y_stride, 
                            starting_x = starting_x, starting_y = row_idx,
                            str_to_find = "MAS") or find_xmas_string(input,
                            x_stride = x_stride, y_stride = y_stride, 
                            starting_x = starting_x, starting_y = row_idx,
                            str_to_find = "SAM"):
                    x_mas_instances += 1
                    
    return x_mas_instances


def find_xmas_string(puzzle_input: list[str],
                     x_stride: int = 1, y_stride: int = 0, 
                     starting_x: int = 0, starting_y: int = 0,
                     str_to_find: str = "XMAS"):

    x = starting_x
    y = starting_y  
    for char_to_find in str_to_find:  
        # Checks assume that the lengtht of each row is the same, as in the provided examples
        if x < 0 or y < 0 or y >= len(puzzle_input) or x >= len(puzzle_input[0]):
            return 0
        else:
            if puzzle_input[y][x] == char_to_find:
                x += x_stride
                y += y_stride
            else:
                return 0
    return 1
        
        

class Test(unittest.TestCase):
    def test_with_provided_example(self):
        with open("inputs/input4_test.txt") as f:
            data = f.read()
        predicted_answer = generate_answer(data)
        expected_anser = 18
        self.assertEqual(expected_anser, predicted_answer)

    
    def test_with_provided_example_part2(self):
        with open("inputs/input4_test.txt") as f:
            data = f.read()
        predicted_answer = generate_answer_part2(data)
        expected_anser = 9
        self.assertEqual(expected_anser, predicted_answer)


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=3, exit=False)

    with open("inputs/input4.txt") as f:
        data = f.read()

    # Part 1
    answer = generate_answer(data)
    print(f"Answer: {answer}")

    # Part 2
    answer = generate_answer_part2(data)
    print(f"Answer: {answer}")


