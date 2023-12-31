#aoc202305.py
import pathlib
from random import seed
import sys
from typing import List

def parse(puzzle_input: str):
    """Parse input."""
    parts = puzzle_input.split('\n\n')
    """
    seeds are the seeds that need to be planted

    maps are in this order:
    1. seed-to-soil
    2. soil-to-fertilizer
    3. fertilizer-to-water
    4. water-to-light
    5. light-to-temperature
    6. temperature-to-humidity
    7. humidity-to-location

    each line in each map contains 3 numbers representing:
    1. destination range start
    2. source range start
    3. range length
    """
    seeds, *maps = parts
    seeds = [int(seed) for seed in seeds.split(':')[1].split()]
    return seeds, maps

def convert_map(map_info: str):
    """Convert map info into a list of tuples."""
    map_data = map_info.split('\n')[1:]
    map_data = [tuple(int(num) for num in line.split()) for line in map_data]
    return map_data

def get_location(seed:int, seed_map: List[tuple]):
    for dest, src, length in seed_map:
        if src <= seed < src + length:
            return seed + dest - src
    return seed


def part1(seeds: List[int], maps: List[str]):
    """Solve part 1.

    Basically we are comparing ranges between two number lines.

    To get the location from src -> dest, we need to:
    1. Check if the seed (input) is within the src range (src <= seed < src + range)
        - If it's not, it's a 1:1 mapping (source 10 => dest 10)
    2. If within source range, we want to find the offset from the start of the range to get the location
        - To get the mapping: seed + dest + src
    """
    # Convert maps into tuples
    seed_maps = [convert_map(map_info) for map_info in maps]
    locations = []
    for seed in seeds:
        for seed_map in seed_maps:
            seed = get_location(seed, seed_map)
        locations.append(seed)
    return min(locations)

def part2(seeds: List[int], maps: List[str]):
    """Solve part 2.
    Can't just extend the list of seeds by the given length with each pair
    because the range of seeds is too large (program will literally not finish).
    Need to figure out how to modify the "get_location" function to work with
    a range of seed inputs rather than a single seed input.
    """
    seed_maps = [convert_map(map_info) for map_info in maps]
    seed_pairs = list(zip(seeds[::2], seeds[1::2]))
    print(seed_pairs)
    locations = []
    for seed in seeds:
        print(seed)
        for seed_map in seed_maps:
            seed = get_location(seed, seed_map)
        locations.append(seed)
    return min(locations)

def solve(puzzle_input: str):
    """Solve the puzzle for the given input."""
    seeds, maps = parse(puzzle_input)
    solution1 = part1(seeds, maps)
    solution2 = part2(seeds, maps)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
