#aoc202307.py
import pathlib
import sys
from typing import List

def parse(puzzle_input: str):
    """Parse input."""
    return [(hand, int(bid)) for line in puzzle_input.splitlines() for hand, bid in (line.split(),)]

def evaluate_hand(line: tuple[str, int]):
    hand, bid = line
    # Translating to ABCDE due to how `sorted` orders characters
    hand = hand.translate(str.maketrans('TJQKA', 'ABCDE'))
    best = max(calculate_type(hand))
    return best, hand, int(bid)

def calculate_type(hand: str):
    hand_counts = map(hand.count, hand)
    return sorted(hand_counts, reverse=True)

def part1(data: List[tuple[str, int]]):
    """Solve part 1.

    Rank the hands based on the order of how good the hand is
    Once the array is in order, take the bid of that hand and multiple it by the rank position

    i.e. [hand1, hand2, hand3, hand4, hand5] => {
        hand1*1 + hand2*2 + hand3*3 + hand4*4 + hand5*5
    }
    """
    evaluated_hands = map(evaluate_hand, data)
    sorted_hands = sorted(evaluated_hands)

    total = 0
    for rank, hand in enumerate(sorted_hands, start=1):
        _, _, bid = hand
        total += rank * bid
    return total


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
