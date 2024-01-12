# https://adventofcode.com/2023/day/3

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [f".{line.strip()}." for line in f.readlines()]

lines.insert(0, "." * 142)
lines.append("." * 142)

symbols = set("".join(lines))

symbols.difference_update(set(".0123456789"))

# with open("input2.txt", "w", encoding="utf-8") as out:
#     for line in lines:
#         out.write(line)
#         out.write("\n")

numbers_on_lines = {line_num: [] for line_num in range(len(lines[1:]))}
for i, line in enumerate(lines[1:]):
    number = []
    hot_indexes = []
    for j, char in enumerate(line):
        if char.isdigit():
            hot_indexes.append(j - 1)
            number.append(char)
            # hot_indexes.append(j)
        else:
            number = []
            hot_indexes = []
        if number != [] and (line[j + 1] == "." or line[j + 1] in symbols):
            hot_indexes.append(j)
            hot_indexes.append(j + 1)
            # hot_indexes.append(j + 2)
            numbers_on_lines[i].append((int("".join(number)), hot_indexes))

# result = 0
# part_numbers = []
# for i, number_line in numbers_on_lines.items():
#     parts_in_line = []
#     for number, hot_indexes in number_line:
#         all_good = False
#         for char in lines[i][hot_indexes[0] : hot_indexes[-1]]:
#             if char in symbols:
#                 all_good = True
#                 break
#         if not all_good:
#             for char in lines[i + 1][hot_indexes[0] : hot_indexes[-1]]:
#                 if char in symbols:
#                     all_good = True
#                     break
#         if not all_good:
#             for char in lines[i + 2][hot_indexes[0] : hot_indexes[-1]]:
#                 if char in symbols:
#                     all_good = True
#                     break
#         if all_good:
#             result += number
#             parts_in_line.append(number)
#     part_numbers.append(parts_in_line)
# print(result)

gearNbCount = [[0 for _ in range(len(lines))] for _ in range(len(lines))]
gearProd = [[1 for _ in range(len(lines))] for _ in range(len(lines))]

result2 = 0
for i, number_line in numbers_on_lines.items():
    for number, hot_indexes in number_line:
        for j in hot_indexes:
            if lines[i][j] == "*":
                gearNbCount[i][j] += 1
                gearProd[i][j] *= number
    for number, hot_indexes in list(numbers_on_lines.values())[i - 2]:
        for j in hot_indexes:
            if lines[i][j] == "*":
                gearNbCount[i][j] += 1
                gearProd[i][j] *= number
    for number, hot_indexes in list(numbers_on_lines.values())[i - 1]:
        for j in hot_indexes:
            if lines[i][j] == "*":
                gearNbCount[i][j] += 1
                gearProd[i][j] *= number


for i, (rowProd, rowCount) in enumerate(zip(gearProd, gearNbCount)):
    for j, (prod, count) in enumerate(zip(rowProd, rowCount)):
        if count == 2:
            result2 += prod
        if count == 0:
            gearNbCount[i][j] = "."

for i, row in enumerate(gearNbCount):
    row = [str(el) for el in row]
    print(i, "".join(row))

print(result2)
