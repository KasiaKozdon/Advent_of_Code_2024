import re
import unittest


def generate_answer(input: str) -> int:
    middle_page_nr = []

    rules = get_rules(input)
    updates = get_page_numbers(input)
    for update in updates:
        if check_if_ordering_correct(update, rules):
            middle_page_nr.append(update[len(update) // 2])

    return sum(middle_page_nr)


def generate_answer_part2(input: str) -> int:
    middle_page_nr = []

    rules = get_rules(input)
    updates = get_page_numbers(input)
    for update in updates:
        if not check_if_ordering_correct(update, rules):
            update = reorder(update, rules)
            middle_page_nr.append(update[len(update) // 2])

    return sum(middle_page_nr)


def get_rules(input: str) -> list[tuple]:
    """Extracts rules of page ordering from the instructions. 
    Returns list of tuples (a, b), where if a and b are both present, a has to be before b"""
    rules = []
    
    rules_description = input.split("\n\n")[0]
    rules_description = rules_description.split("\n")
    for rule in rules_description:
        first, second = re.findall(r"\d+", rule)
        rules.append((int(first), int(second)))

    return rules


def get_page_numbers(input: str) -> list[list[int]]:
    """Extracts the sets of pages requested for each version of the manual."""
    pages = []
    pages_description_paragraph = input.split("\n\n")[1]
    pages_description_paragraph = pages_description_paragraph.split("\n")
    for pages_description_line in pages_description_paragraph:
        pages_nrs = re.findall("\d+", pages_description_line)
        if len(pages_nrs):
            pages.append([int(i) for i in pages_nrs])

    return pages


def check_if_ordering_correct(page_numbers: list[int], rules: list[tuple]) -> bool:
    for (preceding_page, following_page) in rules:
        if any([page_nr == preceding_page for page_nr in page_numbers]):
            preceding_page_idx = page_numbers.index(preceding_page)
            if any([page_nr == following_page for page_nr in page_numbers[:preceding_page_idx]]):
                return False
    return True


def reorder(page_numbers: list[int], rules: list[tuple]) -> list[int]:
    while not check_if_ordering_correct(page_numbers, rules):
        for (preceding_page, following_page) in rules:
            if any([page_nr == preceding_page for page_nr in page_numbers]):
                preceding_page_idx = page_numbers.index(preceding_page)
                if any([page_nr == following_page for page_nr in page_numbers[:preceding_page_idx]]):
                    page_numbers.remove(following_page)
                    page_numbers.insert(preceding_page_idx+1, following_page)
    return page_numbers


class Test(unittest.TestCase):
    def test_with_provided_example_find_correct(self):
        with open("inputs/input5_test.txt") as f:
            data = f.read()

        rules = get_rules(data)
        updates = get_page_numbers(data)
        predicted_answer = [check_if_ordering_correct(update, rules) for update in updates]
        expected_answer = [True, True, True, False, False, False]
        self.assertEqual(expected_answer, predicted_answer)

    def test_with_provided_example(self):
        with open("inputs/input5_test.txt") as f:
            data = f.read()

        predicted_answer = generate_answer(data)
        expected_answer = 143
        self.assertEqual(expected_answer, predicted_answer)


    def test_with_provided_example_part2(self):
        with open("inputs/input5_test.txt") as f:
            data = f.read()

        predicted_answer = generate_answer_part2(data)
        expected_answer = 123
        self.assertEqual(expected_answer, predicted_answer)
     


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False, verbosity=3)

    with open("inputs/input5.txt") as f:
        data = f.read()

    # Part 1
    answer = generate_answer(data)
    print(f"Answer for part 1: {answer}")

    # Part 2
    answer = generate_answer_part2(data)
    print(f"Answer for part 2: {answer}")