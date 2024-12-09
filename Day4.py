import unittest


def generate_answer(input: str) -> int:
    input = input.rstrip().split("\n")

    xmas_instances = 0
    for row_idx, row in enumerate(input):
        for letter_idx, letter in enumerate(row):
            for x_stride in [-1, 0, 1]:
                for y_stride in [-1, 0, 1]:
                    if letter == "X":
                        xmas_instances += find_xmas_string(input,
                        x_stride = x_stride, y_stride = y_stride, 
                        starting_x = letter_idx, starting_y = row_idx,
                        str_to_find = "XMAS")
                    
    return xmas_instances


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


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=3, exit=False)

    with open("inputs/input4.txt") as f:
        data = f.read()

    # Part 1
    answer = generate_answer(data)
    print(f"Answer: {answer}")


