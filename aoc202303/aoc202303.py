#aoc2023_template.py
import pathlib
import sys
from typing import List

def parse(puzzle_input: str):
    """Parse input."""
    return [list(line) for line in puzzle_input.split('\n')]

def part1(data: list[list[str]]):
    """Solve part 1."""
    sum_of_valid_groups = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]  # right, down, left, up, right-down, left-up, right-up, left-down
    num_group_coords: List[List[tuple[int, int]]] = []
    for i in range(len(data)):
        num_group: List[tuple[int, int]] = []
        for j in range(len(data[i])):
            if data[i][j].isdigit():
                num_group.append((i,j))
            else:
                if len(num_group) > 0:
                    num_group_coords.append(num_group)
                    num_group = []

    for num_group in num_group_coords:
        valid_group = False
        for i, j in num_group:
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(data) and 0 <= nj < len(data[i]) and data[ni][nj] not in ["."] and (ni, nj) not in num_group:
                    valid_group = True
        if valid_group:
            sum_of_valid_groups += int("".join(data[i][j] for i, j in num_group))
    # Keeps saying input is too low...
    return sum_of_valid_groups

def part2(data: list[list[str]]):
    """Solve part 2."""


def solve(puzzle_input):
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
