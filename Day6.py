import typing
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
    movement_history = mark_visit_on_the_map(movement_history, y_coord, x_coord, marker_of_visit)
    while (0 <= x_coord < maze_width - 1) and (0 <= y_coord < maze_height - 1):
        next_x_coord = x_coord + x_heading
        next_y_coord = y_coord + y_heading
        if check_if_accessible(data, next_x_coord, next_y_coord):
            nr_steps += 1
            movement_history = mark_visit_on_the_map(movement_history, y_coord, x_coord, marker_of_visit)
            x_coord = next_x_coord
            y_coord = next_y_coord
        else:
            x_heading, y_heading = change_heading(x_heading, y_heading)

    movement_history = mark_visit_on_the_map(movement_history, y_coord, x_coord, marker_of_visit)
    nr_locations_visited = count_char_occurences(movement_history, marker_of_visit)
    return nr_locations_visited


def generate_answer_part2(data):
    data = data.strip("\n\n").split("\n")
    maze_width = len(data[0])
    maze_height = len(data)
    start_x_coord, start_y_coord = find_location(data)
    start_x_heading, start_y_heading = find_heading(data, start_x_coord, start_y_coord)

    # Loop that places one obstruction at each location there is none
    nr_infinite_loops = 0
    for row_idx, row in enumerate(data):
         for col_idx, letter in enumerate(row):
            if (col_idx, row_idx) != (start_x_coord, start_y_coord):
                if check_if_accessible(data, col_idx, row_idx):
                    altered_map = add_obstacle_to_map(data, row_idx, col_idx)
                    
                    x_coord, y_coord = start_x_coord, start_y_coord
                    x_heading, y_heading = start_x_heading, start_y_heading
                    movement_history = [(y_coord, x_coord)]  

                    while (0 <= x_coord < maze_width - 1) and (0 <= y_coord < maze_height - 1):
                        next_x_coord = x_coord + x_heading
                        next_y_coord = y_coord + y_heading
                        if check_if_accessible(altered_map, next_x_coord, next_y_coord):
                            x_coord = next_x_coord
                            y_coord = next_y_coord
                            movement_history.append((y_coord, x_coord))
                            if detect_loop(movement_history):
                                nr_infinite_loops += 1 
                                break
                        else:
                            x_heading, y_heading = change_heading(x_heading, y_heading)

    return nr_infinite_loops


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


def mark_visit_on_the_map(movement_history: list[str], y_coord: int, x_coord: int, marker_of_visit: str = "x"):
    return generate_altered_map(movement_history, y_coord, x_coord, marker_of_visit)


def add_obstacle_to_map(maze: list[str], y_coord: int, x_coord: int, marker_to_place: str = "#"):
    return generate_altered_map(maze, y_coord, x_coord, marker_to_place)


def generate_altered_map(map: list[str], y_coord: int, x_coord: int, marker_to_place: str):
    new_map = map.copy()
    new_map[y_coord] = new_map[y_coord][:x_coord] + marker_to_place + new_map[y_coord][x_coord+1:]
    return new_map


def count_char_occurences(maze: list[str], symbol_to_count: str = 'x') -> int:
    occurences = 0
    for row in maze:
        occurences += row.count(symbol_to_count)
    return occurences


def detect_loop(movement_history: list[tuple[int, int]]) -> bool:
    # check if new location already exists
    current_location = movement_history[-1]
    previous_location = movement_history[-2]
    other_locations = movement_history[:-2]

    if current_location in other_locations:
         if previous_location in other_locations:
            for idx, location in enumerate(other_locations):
                if location == previous_location:
                    if other_locations[idx + 1] == current_location:
                        return True
                              
    return False          

class Test(unittest.TestCase):
    def test_with_provided_example(self):
        with open("inputs/input6_test.txt") as f:
            data = f.read()

        expected_answer = 41
        predicted_answer = generate_answer(data)
        self.assertEqual(expected_answer, predicted_answer)

    def test_with_provided_example_part2(self):
        with open("inputs/input6_test.txt") as f:
            data = f.read()

        expected_answer = 6
        predicted_answer = generate_answer_part2(data)
        self.assertEqual(expected_answer, predicted_answer)


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=3, exit=False)

    with open("inputs/input6.txt") as f:
        data = f.read()
    
    # Part 1
    answer = generate_answer(data)
    print(f"Answer for part 1: {answer}")

    # Part 2
    answer = generate_answer_part2(data)
    print(f"Answer for part 2: {answer}")