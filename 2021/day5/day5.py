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

"""
--- Day 5: Hydrothermal Venture ---

You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

    An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

Your puzzle answer was 7644.
--- Part Two ---

Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

    An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....

You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?

Your puzzle answer was 18627.

Both parts of this puzzle are complete! They provide two gold stars: **
"""
