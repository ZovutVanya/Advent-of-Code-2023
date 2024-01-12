# https://adventofcode.com/2023/day/6

with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# times = lines[0].strip().split()[1:]
# distances = lines[1].strip().split()[1:]

# t2d = {int(time): int(distance) for time, distance in zip(times, distances)}

# result = 1
# for time, record in t2d.items():
#     distances = map(lambda s: s * (time - s), range(time + 1))
#     winning_distances = filter(lambda d: d > record, distances)
#     ways_of_winning = len(tuple(winning_distances))
#     result *= ways_of_winning
# print(result)

time = int("".join(lines[0].strip().split()[1:]))
record = int("".join(lines[1].strip().split()[1:]))

print(time)
print(record)

distances = map(lambda s: s * (time - s), range(time + 1))
winning_distances = filter(lambda d: d > record, distances)
ways_of_winning = len(tuple(winning_distances))
print(ways_of_winning)
