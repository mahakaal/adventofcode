import re

matcher = re.compile(r'^(\d+)\s+(\d+)$')
list1, list2 = [], []

with open ('puzzle.txt') as f:
    for line in f.read().strip().split('\n'):
        match = matcher.match(line)
        if match:
            list1.append(int(match.group(1)))
            list2.append(int(match.group(2)))

        continue

list1.sort()
list2.sort()

distance = sum(abs(a - b) for a, b in zip(list1, list2))
print(distance)

frequency = sum(x * list2.count(x) for x in list1)
print(frequency)
