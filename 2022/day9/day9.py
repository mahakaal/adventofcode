from math import sqrt

filename = 'puzzle.txt'


def to_list(s: str) -> [str, int]:
    a, b = s.split()
    return [a, int(b)]


with open(filename, 'r') as file:
    data = [to_list(line) for line in file.read().strip().split('\n')]


def solve(rope: [[int]], input_data: [str]) -> [{}]:
    visited = [{(0, 0)} for _ in range(len(rope) - 1)]

    for index, line in zip(range(len(input_data)), input_data):
        d, step = line
        i, j = rope[0]

        match d:
            case 'D':
                rope[0] = [i - step, j]
            case 'L':
                rope[0] = [i, j - step]
            case 'R':
                rope[0] = [i, j + step]
            case 'U':
                rope[0] = [i + step, j]
            case _:
                break

        for _ in range(step):
            for k in range(1, len(rope)):
                distance = round(sqrt((rope[k - 1][0] - rope[k][0]) ** 2 + (rope[k - 1][1] - rope[k][1]) ** 2))

                if distance <= 1:
                    break

                if rope[k - 1][0] == rope[k][0]:  # Same row, different column
                    if rope[k - 1][1] > rope[k][1]:
                        rope[k][1] += 1
                    elif rope[k - 1][1] < rope[k][1]:
                        rope[k][1] -= 1
                elif rope[k - 1][1] == rope[k][1]:  # Same column, different row
                    if rope[k - 1][0] > rope[k][0]:
                        rope[k][0] += 1
                    elif rope[k - 1][0] < rope[k][0]:
                        rope[k][0] -= 1
                elif distance > 1:  # Different coordinates, calculate diagonal direction if diff > 1
                    if rope[k - 1][0] > rope[k][0] and rope[k - 1][1] > rope[k][1]:
                        rope[k] = [rope[k][0] + 1, rope[k][1] + 1]
                    elif rope[k - 1][0] < rope[k][0] and rope[k - 1][1] < rope[k][1]:
                        rope[k] = [rope[k][0] - 1, rope[k][1] - 1]
                    elif rope[k - 1][0] > rope[k][0] and rope[k - 1][1] < rope[k][1]:
                        rope[k] = [rope[k][0] + 1, rope[k][1] - 1]
                    elif rope[k - 1][0] < rope[k][0] and rope[k - 1][1] > rope[k][1]:
                        rope[k] = [rope[k][0] - 1, rope[k][1] + 1]

                visited[k - 1].add((rope[k][0], rope[k][1]))

    return visited


def part1(input_data: [str]) -> int:
    return len(solve([[0, 0], [0, 0]], input_data)[-1])


def part2(input_data: [str]) -> int:
    return len(solve([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], input_data)[-1])


print(f"Part 1: %d" % part1(data))
print(f"Part 2: %d" % part2(data))
