filename = 'test-data.txt'

with open(filename, 'r') as file:
    data = [line for line in file.read().strip().split('\n')]

cycle = x = 1
cycles = {cycle: x}

for instruction in data:
    match instruction.split():
        case ['addx', step]:
            cycles.setdefault(cycle, x)
            cycles.setdefault(cycle + 1, x)
            x += int(step)
            cycle += 2
        case _:
            cycles.setdefault(cycle, x)
            cycle += 1

points = [20, 60, 100, 140, 180, 220]
total = sum(cycles[p] * p for p in points)

print(total)
