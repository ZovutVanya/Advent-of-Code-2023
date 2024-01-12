# https://adventofcode.com/2023/day/4

with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

cards = dict()
for line in lines:
    card_num, numbers = line.split(":")
    card_num = int(card_num.split(" ")[-1])

    numbers = numbers.strip().split(" | ")
    numbers = [[int(num) for num in nums.split()] for nums in numbers]

    cards[card_num] = numbers


result = 0
card2card = dict()
for numbers in cards.values():
    win_nums, elf_nums = numbers
    counter = 0
    points = 0
    for elf_num in elf_nums:
        if elf_num in win_nums:
            points = 2**counter
            counter += 1
    result += points
    won_cards = [card_num + i for i in range(counter + 1)][1:]
    card2card[card_num] = won_cards
print(f"Part One: {result}")


cards_instances_count = [1] * len(card2card)
total_sum = 0
for card_id, won_cards in enumerate(card2card.values()):
    matches = len(won_cards)

    total_sum += cards_instances_count[card_id]

    for index in range(card_id + 1, card_id + matches + 1):
        cards_instances_count[index] += cards_instances_count[card_id]

print(f"Part Two: {total_sum}")
