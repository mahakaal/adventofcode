def read_file(filename):
    with open(filename, 'r') as file:
        return [list(map(int, list(line.strip()))) for line in file.read().strip().split("\n")]


def extract_window(x, y, matrix):
    if (x, y) == (0, 0):
        return [matrix[x+1][y], matrix[x][y+1]]
    elif (x, y) == (len(matrix) - 1, len(matrix[0]) - 1):
        return [matrix[x-1][y], matrix[x-1][y-1]]
    elif (x, y) == (0, len(matrix[0]) - 1):
        return [matrix[x][y-1], matrix[x+1][y]]
    elif y == len(matrix[0]) - 1:
        return [matrix[x-1][y], matrix[x][y-1], matrix[x+1][y]]
    elif (x, y) == (len(matrix) - 1, 0):
        return [matrix[x-1][y], matrix[x][y+1]]
    elif x == len(matrix) - 1:
        return [matrix[x-1][y], matrix[x][y-1], matrix[x][y+1]]
    elif x == 0:
        return [matrix[x][y-1], matrix[x+1][y], matrix[x][y+1]]
    elif y == 0:
        return [matrix[x-1][y], matrix[x+1][y], matrix[x][y+1]]

    return [matrix[x-1][y], matrix[x][y-1], matrix[x+1][y], matrix[x][y+1]]


def check_basin(matrix, x, y, visited_nodes, r_len, c_len):
    if x < 0 or y < 0 or x > r_len or y > c_len \
            or matrix[x][y] == 9 \
            or (x, y) in visited_nodes:
        return

    visited_nodes.append((x, y))

    check_basin(matrix, x, y + 1, visited_nodes, r_len, c_len)
    check_basin(matrix, x, y - 1, visited_nodes, r_len, c_len)
    check_basin(matrix, x - 1, y, visited_nodes, r_len, c_len)
    check_basin(matrix, x + 1, y, visited_nodes, r_len, c_len)


heightmap = read_file("puzzle.txt")
heights_sum = []
for i in range(0, len(heightmap)):
    for j in range(0, len(heightmap[0])):
        cur = heightmap[i][j]
        window = extract_window(i, j, heightmap)
        if cur < min(window):
            heights_sum.append((i, j, cur))

print(sum(value + 1 for _, _, value in heights_sum))

basins = []
for heights in heights_sum:
    i, j, z = heights
    visited = []
    check_basin(heightmap, i, j, visited, len(heightmap) - 1, len(heightmap[0]) - 1)
    basins.append(len(visited))

basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])


"""
--- Day 9: Smoke Basin ---

These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678

Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

Your puzzle answer was 423.
--- Part Two ---

Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678

The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678

The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?

Your puzzle answer was 1198704.

Both parts of this puzzle are complete! They provide two gold stars: **
"""
