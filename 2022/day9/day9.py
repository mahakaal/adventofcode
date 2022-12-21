from math import sqrt

filename = 'puzzle.txt'


def to_list(s: str) -> [str, int]:
    a, b = s.split()
    return [a, int(b)]


with open(filename, 'r') as file:
    data = [to_list(line) for line in file.read().strip().split('\n')]

start = H = T = [0, 0]
visited = {'P0,0': 1}

for line in data:
    d, step = line
    i, j = H

    match d:
        case 'D':
            H = [i - step, j]
        case 'L':
            H = [i, j - step]
        case 'R':
            H = [i, j + step]
        case 'U':
            H = [i + step, j]
        case _:
            break

    for _ in range(step):
        distance = round(sqrt((H[0] - T[0])**2 + (H[1] - T[1])**2))

        if distance <= 1:
            continue

        if H[0] == T[0]:    # Same row, different column
            if H[1] > T[1]:
                T[1] += 1
            elif H[1] < T[1]:
                T[1] -= 1
        elif H[1] == T[1]:    # Same column, different row
            if H[0] > T[0]:
                T[0] += 1
            elif H[0] < T[0]:
                T[0] -= 1
        elif distance > 1:    # Different coordinates, calculate diagonal direction if diff > 1
            if H[0] > T[0] and H[1] > T[1]:
                T = [T[0] + 1, T[1] + 1]
            elif H[0] < T[0] and H[1] < T[1]:
                T = [T[0] - 1, T[1] - 1]
            elif H[0] > T[0] and H[1] < T[1]:
                T = [T[0] + 1, T[1] - 1]
            elif H[0] < T[0] and H[1] > T[1]:
                T = [T[0] - 1, T[1] + 1]

        n = f'P%d,%d' % (T[0], T[1])
        t = visited.setdefault(n, 1)
        if t > 1:
            visited[n] += 1

print(f"Part 1: %d" % len(visited))
