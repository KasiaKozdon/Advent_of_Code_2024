import unittest


def generate_answer(data):
    data = data.strip("\n\n").split("\n")
    movement_history = data.copy()
    maze_width = len(data[0])
    maze_height = len(data)

    x_coord, y_coord = find_location(data)
    x_heading, y_heading = find_heading(data, x_coord, y_coord)

    nr_steps = 1
    marker_of_visit = 'x'
    movement_history = mark_visit(movement_history, y_coord, x_coord, marker_of_visit)
    while (0 <= x_coord < maze_width - 1) and (0 <= y_coord < maze_height - 1):
        next_x_coord = x_coord + x_heading
        next_y_coord = y_coord + y_heading
        if check_if_accessible(data, next_x_coord, next_y_coord):
            nr_steps += 1
            movement_history = mark_visit(movement_history, y_coord, x_coord, marker_of_visit)
            x_coord = next_x_coord
            y_coord = next_y_coord
        else:
            x_heading, y_heading = change_heading(x_heading, y_heading)

    movement_history = mark_visit(movement_history, y_coord, x_coord, marker_of_visit)
    nr_locations_visited = count_char_occurences(movement_history, marker_of_visit)
    return nr_locations_visited


def find_location(maze: list[str]) -> tuple[int]:
    possible_starting_symbols = ["<", ">", "v", "^"]
    for row_idx, row in enumerate(maze):
         for col_idx, letter in enumerate(row):
              if any([symbol == letter for symbol in possible_starting_symbols]):
                   return (col_idx, row_idx)                


def find_heading(maze: list[str], x_coord: int, y_coord: int) -> tuple[int]:
    traveler_symbol = maze[y_coord][x_coord]
    if traveler_symbol == "^":
            return (0, -1)
    elif traveler_symbol == "v":
            return (0, 1)
    elif traveler_symbol == ">":
            return (1, 0)
    elif traveler_symbol == "<":
            return (0, -1)
    else:
         print(f"Unexpected character {traveler_symbol} at the starting location {x_coord}, {y_coord}.")


def check_if_accessible(maze: list[str], x_coord: int, y_coord: int) -> bool:
    blockage_sign = "#"
    return maze[y_coord][x_coord] != blockage_sign


def change_heading(x_heading: int, y_heading: int) -> tuple[int]:
    """
    Turn by 90 degrees right.
    """
    new_y_heading = x_heading
    new_x_heading = -y_heading
    return (new_x_heading, new_y_heading)


def mark_visit(movement_history: list[str], y_coord: int, x_coord: int, marker_of_visit: str):
    movement_history[y_coord] = movement_history[y_coord][:x_coord] + marker_of_visit + movement_history[y_coord][x_coord+1:]
    return movement_history


def count_char_occurences(maze: list[str], symbol_to_count: str = 'x') -> int:
    occurences = 0
    for row in maze:
        occurences += row.count(symbol_to_count)
    return occurences

class Test(unittest.TestCase):
    def test_with_provided_example(self):
        with open("inputs/input6_test.txt") as f:
            data = f.read()

        expected_answer = 41
        predicted_answer = generate_answer(data)
        self.assertAlmostEqual(expected_answer, predicted_answer)


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=3, exit=False)

    with open("inputs/input6.txt") as f:
        data = f.read()
    
    # Part 1
    answer = generate_answer(data)
    print(f"Answer for part 1: {answer}")