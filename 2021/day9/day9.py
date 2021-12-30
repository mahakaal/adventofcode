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
