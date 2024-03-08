#!/usr/bin/env python3
import re

SYMBOLS = "!@#$%^&*()_+=-[]{}/"
NUMBER_PATTERN = re.compile(r"(\d{1,4})")
NUMBERS = '0123456789'

def read_file(path: str):
    with open(path) as f:
        data = [l.strip("\n") for l in f.readlines()]
    return data


def get_context_lines(data: list, line_number: int):
    """
    Get the lines around the current line.
    """
    current_line = data[line_number]
    if line_number == 0:
        line_before = "." * len(current_line)
        line_after = data[line_number + 1]
        return [line_before, current_line, line_after]
    elif line_number == len(data) - 1:
        line_before = data[line_number - 1]
        line_after = "." * len(data[line_number])
        return [line_before, current_line, line_after]
    else:
        line_before = data[line_number - 1]
        line_after = data[line_number + 1]
        return [line_before, current_line, line_after]


def check_lines(line_before: str, current_line: str, line_after: str):
    """
    Loop over each item in each line. If the index of either the line
    after or the line before has a symbol BEFORE, ON, or AFTER the number,
    add it as a part number.
    """
    # for idx, cb, cc, ca in zip(
    #     range(0, len(current_line)), line_before, current_line, line_after
    # ):
    #     pass
    for idx, c in enumerate(current_line):
        indices = []
        numbers = []
        num = ''
        if c in NUMBERS:
            num += c
            indices.append(idx)
        elif num != '' and c == '.':
            numbers.append(int(num))



# loop over each line
# Check line before, at index of each number, for symbol
# Check line after,  at index of each number, for symbol
# Check current line before and after each number for symbol
if __name__ == "__main__":
    data = read_file("./input.txt")
    print(data)
    # print(f'Length of data: {len(data)}') #140


"""
Example:

467..114..
...*......
..35..633.
......#...

Part numbers:
467, 35, 633
Not 114.
For adjacent: Check idx of each number +/- 1 on line above and line below.
"""
