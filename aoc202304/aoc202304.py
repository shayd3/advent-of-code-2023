#aoc202304.py
import pathlib
import sys
from typing import List

def parse(puzzle_input: str):
    """Parse input."""
    return puzzle_input.splitlines()

def part1(data: List[str]):
    """Solve part 1."""
    points = 0
    for line in data:
        card, numbers = line.split(":")
        winning_numbers, curr_numbers = numbers.split("|")
        winning_numbers = [int(x) for x in winning_numbers.split()]
        curr_numbers = [int(x) for x in curr_numbers.split()]
        print(card, winning_numbers, curr_numbers)

        current_winning_num_count = len(set(winning_numbers) & set(curr_numbers))
        if current_winning_num_count > 0:
            points += 2**(current_winning_num_count-1)
    return points

def part2(data: List[str]):
    """Solve part 2."""


def solve(puzzle_input: str):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
