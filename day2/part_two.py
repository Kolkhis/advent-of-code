#!/usr/bin/env python3
import re

r"""
Part 2
In each game you played, what is the fewest
number of cubes of each color that could have
been in the bag to make the game possible?

The power of a set of cubes is equal to the numbers of red,
green, and blue cubes multiplied together.

For each game, find the minimum set of cubes that must have been present.
What is the sum of the power of these sets?
"""


def sanitize_bag(dirty_bag):
    clean_bag = []
    for item in dirty_bag:
        if ";" in item:
            separated_items = item.split(";")
            for i in separated_items:
                clean_bag.append(i.strip())
        else:
            clean_bag.append(item.strip())
    return clean_bag

def check_line(line):
    cubes = {"red": 0, "green": 0, "blue": 0}
    bag_contents = sanitize_bag(line.split(":")[1].split(","))
    cube_pattern = re.compile(r"(\d{1,2})[ ;](green|red|blue)")
    for item in bag_contents:
        match = re.match(cube_pattern, item)
        if match is not None:
            count = int(match.group(1))
            color = match.group(2)
            if cubes[color] == 0 or cubes[color] < count:
                cubes[color] = count
    total = 1
    for color in cubes.keys():
        total *= cubes[color]
    return total


def get_data(path):
    with open(path) as f:
        data = [line.strip("\n") for line in f.readlines()]
    return data


if __name__ == "__main__":
    file = "input.txt"
    d = get_data(file)
    power_sum = 0
    for line in d:
        power_sum += check_line(line)
    print(f"Sum of the power of the sets: {power_sum}")

