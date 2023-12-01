#!/usr/bin/env python3


nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',]

def read_input(path: str) -> list:
    with open(path) as f:
        data = f.readlines()
        print("Length of data list:")
        print(len(data))
    return clean_data(data)


def clean_data(data: list) -> list:
    cleaned_data = []
    for item in data:
        if item == '\n':
            continue
        cleaned_data.append(item.strip('\n'))
    return cleaned_data

def get_first_digit(item: str):
    first = None
    for char in item:
        if first is None and char in nums:
            first = char
            break
    return first

def get_last_digit(item: str):
    last = None
    for char in item[::-1]:
        if last is None and char in nums:
            last = char
            break
    return last


def get_digits(item: str):
    first = get_first_digit(item)
    last = get_last_digit(item)
    if first is not None and last is not None:
        return first, last
    return '0', '0'
            


if __name__ == '__main__':
    data = read_input('./input.txt')
    entries = []
    for item in data:
        first_digit, last_digit = get_digits(item)
        numberized = int(first_digit + last_digit)
        entries.append(numberized)
    print(f"Sum of all entries: {sum(entries)}")

