import re
from typing import List


def read_file(file_name: str) -> List:
    with open(file_name, "r") as file:
        return [[tuple(map(lambda x: int(x), re.split(',', points))) for points in row.split(" -> ")]
                for row in file.read().strip().split("\n")]


def generate_linspace(cols: int) -> List:
    return [[0] * cols for _ in range(0, cols)]


def get_straight_lines(lines: List) -> List:
    return list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], lines))


def part1(lines: List):
    plane = generate_linspace(1000)

    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]

        if x1 == x2:
            from_y, to_y = y1 if y1 < y2 else y2, (y1 + 1) if y1 > y2 else (y2 + 1)
            for y in range(from_y, to_y):
                plane[x1][y] += 1
        elif y1 == y2:
            from_x, to_x = x1 if x1 < x2 else x2, (x1 + 1) if x1 > x2 else (x2 + 1)
            for x in range(from_x, to_x):
                plane[x][y1] += 1
        else:
            for i in range(abs(x2 - x1)):
                x, y = x1 + i if x1 < x2 else x1 - i, y1 + i if y1 < y2 else y1 - i
                plane[x][y] += 1

            # while True:
            #     plane[x][y] += 1
            #
            #     if x == x2 and y == y2:
            #         break
            #
            #     if x <= x2:
            #         x += 1
            #     elif x >= x2:
            #         x -= 1
            #
            #     if y <= y2:
            #         y += 1
            #     elif y >= y2:
            #         y -= 1

    return sum(elem > 1 for row in plane for elem in row)


print("Part 1", part1(get_straight_lines(read_file("puzzle.txt"))))
print("Part 2", part1(read_file("puzzle.txt")))
