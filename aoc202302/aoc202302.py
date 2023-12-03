#aoc202302.py
import pathlib
import sys
from typing import List

bagOfCubes = {
    "red": {
        "total_in_bag": 12
    },
    "green": {
        "total_in_bag": 13
    },
    "blue": {
        "total_in_bag": 14
    }
}

def parse(puzzle_input):
    """Parse input."""
    record_of_games = {}
    for gameNumber,line in enumerate(puzzle_input.split('\n')):
        record_of_games[f"game{gameNumber}"] = {}
        game = line.split(": ")[-1]
        gameSets = game.split("; ")
        for setNumber,gameSet in enumerate(gameSets):
            record_of_games[f"game{gameNumber}"][f"set{setNumber}"] = {}
            die_revealed = gameSet.split(", ")
            for die in die_revealed:
                die_count = die.split(" ")[0]
                die_color = die.split(" ")[1]
                record_of_games[f"game{gameNumber}"][f"set{setNumber}"][die_color] = die_count
    return record_of_games

def part1(record_of_games: dict):
    """Solve part 1."""
    valid_game_id_sum = 0
    for game in record_of_games.keys():
        is_valid_game = True
        for gameSet in record_of_games[game].keys():
            for color in record_of_games[game][gameSet].keys():
                if int(record_of_games[game][gameSet][color]) > bagOfCubes[color]["total_in_bag"]:
                    is_valid_game = False
        if is_valid_game:
            valid_game_id_sum += int(game.split("game")[-1]) + 1
    return valid_game_id_sum


def part2(record_of_games: dict):
    """Solve part 2.
    Get total of the minimum amount of cubes in a game that make the game possible"""
    power_of_cubes_sum = 0
    for game in record_of_games.keys():
        min_possible_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for gameSet in record_of_games[game].keys():
            for color in record_of_games[game][gameSet].keys():
                if min_possible_cubes[color] < int(record_of_games[game][gameSet][color]):
                    min_possible_cubes[color] = int(record_of_games[game][gameSet][color])
        power_of_cubes = min_possible_cubes["red"] * min_possible_cubes["green"] * min_possible_cubes["blue"]
        power_of_cubes_sum += power_of_cubes

    return power_of_cubes_sum



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
