#aoc202307.py
import pathlib
import sys
from typing import List

def parse(puzzle_input: str):
    """Parse input."""
    return [(hand, int(bid)) for line in puzzle_input.splitlines() for hand, bid in (line.split(),)]

def part1(data: List[tuple[str, int]]):
    """Solve part 1."""


def part2(data: List[tuple[str, int]]):
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
        print("Part 1:", solutions[0])
        print("Part 2:", solutions[1])
