#aoc2023_template.py
import pathlib
import sys
from typing import List

def parse(puzzle_input: str):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]

def part1(data: List[str]):
    """Solve part 1."""


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
