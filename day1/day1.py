# https://adventofcode.com/2023/day/1

import re


with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

digits = {
    "one": "on1e",
    "two": "tw2o",
    "three": "thr3ee",
    "four": "fo4ur",
    "five": "fi5ve",
    "six": "s6ix",
    "seven": "s7even",
    "eight": "e8ight",
    "nine": "ni9ne",
}


def find_digits(text: str) -> str:
    for digit in digits:
        text = re.sub(digit, str(digits[digit]), text)

    return text


lines = [find_digits(line) for line in lines]


numbers = []
for line in lines:
    int_list = []
    for char in line:
        try:
            char = int(char)
            int_list.append(str(char))
        except Exception:
            continue

    numbers.append(int_list)

numbers = ["".join(number) for number in numbers]
numbers = [str(int(number[0] + number[-1])) for number in numbers]

numbers = [
    int(number) if len(number) == 2 else int(number + number) for number in numbers
]

print(sum(numbers))
