#aoc202301.py
import pathlib
import sys
import re
from typing import List

'''
Replacements for part 2. Used for when words share a common first/last letter
i.e. oneight, eightwo, etc.
'''
replacements = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

def getCalibrationLevelSum(data: List[str]):
    sum = 0
    for line in data:
        numbers = []
        for char in line:
            if char.isnumeric():
                numbers.append(int(char))
        if len(numbers) != 0:
            firstNumber = int(numbers[0])
            lastNumber = int(numbers[-1])
            concatNumber = int(str(firstNumber) + str(lastNumber))
            print(f"Concat number: {concatNumber}")
            sum = sum + concatNumber
    return sum

def convertIntWords(data: List[str]):
    for i,line in enumerate(data):
        newLine = line
        for key in replacements.keys():
            if key in newLine:
                newLine = newLine.replace(key, replacements[key])
                data[i] = newLine
                print(f"key found in line. Old line: {line}, new line: {newLine}")
    return data


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]

def part1(data: List[str]):
    """Solve part 1."""
    return  getCalibrationLevelSum(data)


def part2(data: List[str]):
    """Solve part 2."""
    return getCalibrationLevelSum(convertIntWords(data))


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
