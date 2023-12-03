#!/usr/bin/env python3
import re

r"""
Part 1
Which games would have been possible if the bag contained only:
12 red cubes,
13 green cubes, and
14 blue cubes?
    \(\d\{1,2}\)\([ ;]green\|red\|blue\)
"""
LIMITS = {"red": 12, "green": 13, "blue": 14}


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
    game_id = line.split(":")[0].split(" ")[1]
    bag_contents = sanitize_bag(line.split(":")[1].split(","))
    cube_pattern = re.compile(r"(\d{1,2})[ ;](green|red|blue)")
    for item in bag_contents:
        match = re.match(cube_pattern, item)
        if match is not None:
            count = int(match.group(1))
            color = match.group(2)
            if count > LIMITS[color]:
                return False, 0
            cubes[color] += count
    return True, game_id


def get_data(path):
    with open(path) as f:
        data = [line.strip("\n") for line in f.readlines()]
    return data


if __name__ == "__main__":
    file = "input.txt"
    d = get_data(file)
    possible_games = 0
    tallies = {}
    for line in d:
        possible, id = check_line(line)
        if possible:
            possible_games += int(id)
    print(f"Number of possible games: {possible_games}")
