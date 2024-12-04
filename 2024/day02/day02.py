reports = []

with open('puzzle.txt') as f:
    for line in f.read().strip().split('\n'):
        reports.append([int(a) for a in line.split(' ')])

safe_reports = 0
safe_range = range(1, 4)
for report in reports:
    safe = False
    mode = None
    for i in range(len(report) -1):
        a, b, diff = report[i], report[i+1], None

        if mode is None:
            if a > b and a - b in safe_range:
                mode = 'decrease'
                continue
            elif b > a and b - a in safe_range:
                mode = 'increase'
                continue
            else:
                safe = False
                break

        if mode == 'decrease':
            diff = a - b
        elif mode == 'increase':
            diff = b - a

        if diff not in safe_range:
            safe = False
            break

        safe = True

    safe_reports += 1 if safe else 0

print(safe_reports)
