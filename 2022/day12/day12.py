import collections

filename = 'puzzle.txt'

with open(filename, 'r') as file:
    data = [[l for l in line] for line in file.read().strip().split()]


def get_adjacent(current: (int, int), cols, rows) -> [(int, int)]:
    col, row = current

    match current:
        case (0, 0):
            return [(0, 1), (1, 0)]
        case (0, x):
            return [(col, row - 1), (col + 1, row)] if x == rows - 1 else [(col, row - 1), (col + 1, row),
                                                                           (col, row + 1)]
        case (y, 0):
            return [(col - 1, row), (col, row + 1)] if y == cols - 1 else [(col - 1, row), (col, row + 1),
                                                                           (col + 1, row)]
        case _:
            if current == (cols - 1, rows - 1):
                return [(col, row - 1), (col - 1, row)]
            elif col == cols - 1:
                return [(col, row - 1), (col - 1, row), (col, row + 1)]
            elif row == rows - 1:
                return [(col, row - 1), (col - 1, row), (col + 1, row)]
            else:
                return [(col, row - 1), (col - 1, row), (col, row + 1), (col + 1, row)]


def bfs(root: (int, int), searched: (int, int), input_data: [[str]]) -> int:
    values = {chr(i): i - 96 for i in range(97, 97 + 26)}
    values['S'] = 1
    values['E'] = 26

    queue, visited = collections.deque(), set()
    queue.append([root])

    while queue:
        path = queue.popleft()
        row, col = path[-1]
        current_height = values[input_data[row][col]]

        if (row, col) not in visited:
            visited.add((row, col))

            if (row, col) == searched:
                return len(path) - 1

            for vertex in get_adjacent((row, col), len(input_data), len(input_data[0])):
                vertex_row, vertex_col = vertex
                vertex_height = values[input_data[vertex_row][vertex_col]]

                if vertex_height <= current_height + 1:
                    path_copy = path[:]
                    path_copy.append(vertex)
                    queue.append(path_copy)


starting, ending = None, None

for r, line in enumerate(data):
    if 'S' in line:
        starting = (r, line.index('S'))

    if 'E' in line:
        ending = (r, line.index('E'))

print(f"Part 1 - %d" % bfs(starting, ending, data))

starts = set((row, col) for row in range(len(data)) for col in range(len(data[0])) if data[row][col] == 'a')
distances = [distance for start in starts if (distance := bfs(start, ending, data)) is not None]

print(f"Part 2 - %d" % min(distances))


"""
--- Day 12: Hill Climbing Algorithm ---

You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?

Your puzzle answer was 350.
--- Part Two ---

As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^

This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?

Your puzzle answer was 349.

Both parts of this puzzle are complete! They provide two gold stars: **
"""
