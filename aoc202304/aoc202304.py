#aoc202304.py
import pathlib
import sys
from typing import List
from collections import defaultdict

def parse(puzzle_input: str):
    """Parse input."""
    return puzzle_input.splitlines()

def parse_cards(card: str):
    card_num, numbers = card.split(":")
    winning_numbers, curr_numbers = numbers.split("|")
    winning_numbers = [int(x) for x in winning_numbers.split()]
    curr_numbers = [int(x) for x in curr_numbers.split()]

    return card_num, winning_numbers, curr_numbers

def part1(data: List[str]):
    """Solve part 1."""
    points = 0
    for line in data:
        _, winning_numbers, curr_numbers = parse_cards(line)
        current_winning_num_count = len(set(winning_numbers) & set(curr_numbers))
        if current_winning_num_count > 0:
            points += 2**(current_winning_num_count-1)
    return points

def part2(data: List[str]):
    """Solve part 2.

    In this part, you just get more copies of a card*n where n is the number of winning numbers
    in that card. We keep track of these instead of points.
    """
    # Consider each "card" as a "type of card" and keep track of how many copies of each type of card we have
    cards = defaultdict(int)
    for i,line in enumerate(data):
        # initalize with 1 card for each since we already have 1 copy of each card
        cards[i] += 1
        _, winning_numbers, curr_numbers = parse_cards(line)
        current_winning_num_count = len(set(winning_numbers) & set(curr_numbers))

        # You get more copies of the next n cards where n is the number of winning numbers
        # So here, we are just adding on to the copy of the next few cards
        for j in range(current_winning_num_count):
            cards[i+1+j] += cards[i]
        print(cards)
    return sum(cards.values())

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
