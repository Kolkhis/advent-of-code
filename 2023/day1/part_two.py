#!/usr/bin/env python3

"""
Check indices of the first words and last words
If the BEGINNING of the FIRST word comes before the first digit, use that
If the END of the LAST word comes AFTER the last digit, use that

My answer: 55343
"""

words = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
digit_dict = {w: n for w, n in zip(words, nums)}


def read_input(path: str) -> list:
    with open(path) as f:
        clean_data = [w.strip("\n") for w in f.readlines() if w != "\n"]
    return clean_data


def get_first_word(item: str):
    matches = {}
    word = ""
    location = 0
    for w in words:
        idx = item.find(w)
        if idx != -1:
            word = w
            location = idx
            matches[word] = location
    if word != "":
        if len(matches) > 1:
            for k, v in matches.items():
                if v < location:
                    word, location = k, v
            return word, location
        return word, location
    return None, None


def get_last_word(item: str)->tuple:
    matches = {}
    word = ""
    location = 0
    for w in words:
        idx = item.rfind(w)
        if idx != -1:
            word = w
            location = idx
            matches[word] = location
    if word != "":
        if len(matches) > 1:
            for k, v in matches.items():
                if v > location:
                    word = k if v > location else word
                    word, location = k, v
            return word, location
        return word, location
    return None, None


def get_first_digit(item: str)->tuple:
    first_digit = None
    location = None
    for idx, char in enumerate(item):
        if first_digit is None and char in nums:
            first_digit = char
            location = idx
            break
    return first_digit, location


def get_last_digit(item: str)->tuple:
    last_digit = None
    location = None
    c = len(item)
    for char in reversed(item):
        c -= 1
        if last_digit is None and char in nums:
            last_digit = char
            location = c
            break
    return last_digit, location


def get_digits(item: str)->tuple:
    first, first_loc = get_first_digit(item)
    last, last_loc = get_last_digit(item)
    if first is not None and last is not None:
        return first, first_loc, last, last_loc
    return "0", 0, "0", 0


def get_string_numbers(item: str)->tuple:
    first_word, first_w_loc = get_first_word(item)
    last_word, last_w_loc = get_last_word(item)
    return first_word, first_w_loc, last_word, last_w_loc


if __name__ == "__main__":
    data = read_input("./input.txt")
    entries = []
    for item in data:
        first_digit, first_dig_loc, last_digit, last_dig_loc = get_digits(item)
        first_word, first_w_loc, last_word, last_w_loc = get_string_numbers(item)

        # To avoid using duplicate words
        word_assigned = False

        # Find the first number
        if first_word is not None:
            if first_dig_loc < first_w_loc:
                first_number = first_digit
            else:
                first_number = digit_dict[first_word]
                word_assigned = True
        else:
            first_number = first_digit

        # Find second number
        if last_word is not None:
            if last_dig_loc < (last_w_loc + len(last_word) - 1):
                if word_assigned and first_w_loc == last_w_loc:
                    last_number = last_digit
                else:
                    last_number = digit_dict[last_word]
            else:
                last_number = last_digit
        else:
            last_number = last_digit
        item_sum = int(first_number + last_number)
        entries.append(item_sum)
    print(f"Sum of all entries: {sum(entries)}")
