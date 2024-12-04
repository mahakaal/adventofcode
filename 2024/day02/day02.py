from copy import deepcopy

reports = []

with open('puzzle.txt') as f:
    for line in f.read().strip().split('\n'):
        reports.append([int(a) for a in line.split(' ')])

def get_safe_reports(row: [int]) -> bool:
    safe = False
    mode = None
    for i in range(len(row) - 1):
        a, b, diff = row[i], row[i + 1], None

        if mode is None:
            if a > b:
                mode = 'decrease'
            elif b > a:
                mode = 'increase'
            else:
                safe = False
                break

        if mode == 'decrease':
            diff = a - b
        elif mode == 'increase':
            diff = b - a

        if 1 <= diff <= 3:
            safe = True
        else:
            safe = False
            break

    return safe


print('part 1: ', sum(get_safe_reports(report) for report in reports))

count = 0
for report in reports:
    count += get_safe_reports(report) or any(get_safe_reports(report[:i] + report[i+1:]) for i in range(len(report)))

print('part 2: ', count)