#aoc202306.py
from functools import reduce
import pathlib
import sys
from typing import List

def parse(puzzle_input: str):
    """Parse input."""
    race_document = puzzle_input.splitlines()
    race_time, race_distance = [race for race in race_document]
    race_time = [int(rt) for rt in race_time.split(":")[1].split()]
    race_distance = [int(rd) for rd in race_distance.split(":")[1].split()]
    races = list(zip(race_time, race_distance))
    return races

def part1(races: List[tuple[int,int]]):
    """Solve part 1.
    Input => tuple[total race time(ms), record distance(mm)]

    Based on the the total time for the race and the record distance, we need
    to figure out how many ways we can beat the record.

    Knowns:
    * If button is NOT held, boat does not move
    * If button is held down for the whole time of the race, boat does not move
    * Boat only moves after button is released
    * For every 1 ms that the button is held, the boat moves 1 mm/ms faster
    * The boat starts at 0 mm/ms
    """
    race_win_possibility_counts = []

    for race_time,race_record_distance in races:
        possibility_count = 0
        for button_hold_time in range(race_time+1):
            travel_time = race_time - button_hold_time
            distance_traveled = travel_time * button_hold_time
            if(distance_traveled > race_record_distance):
                possibility_count += 1
        print(possibility_count)
        race_win_possibility_counts.append(possibility_count)

    return reduce(lambda x,y: x*y, race_win_possibility_counts)

def part2(data: List[tuple[int,int]]):
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
