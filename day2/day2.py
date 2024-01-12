# https://adventofcode.com/2023/day/2

from functools import reduce


with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

games = dict()
for line in lines:
    line = line.strip()
    game, reveals = line.split(": ")
    game = game.split(" ")[1]
    reveals = reveals.split("; ")
    reveals = [reveal.split(", ") for reveal in reveals]
    for i, reveal in enumerate(reveals):
        reveal_dict = dict()
        for cc in reveal:
            count, color = cc.split(" ")
            reveal_dict[color] = int(count)
        reveals[i] = reveal_dict
    games[int(game)] = reveals

# cubes = {"red": 12, "green": 13, "blue": 14}
# result1 = 0
# for game, reveals in games.items():
#     game_possible = True
#     for reveal in reveals:
#         for color, count in reveal.items():
#             if count > cubes[color]:
#                 game_possible = False
#                 break
#     if game_possible:
#         result1 += game
# print(result1)

result2 = 0
for game, reveals in games.items():
    min_colors = {"red": 0, "green": 0, "blue": 0}
    for reveal in reveals:
        for color, count in reveal.items():
            if count > min_colors[color]:
                min_colors[color] = count
    power_of_cubes = reduce((lambda x, y: x * y), min_colors.values())
    result2 += power_of_cubes
print(result2)
