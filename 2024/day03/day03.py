import re

with open("puzzle.txt") as f:
    memory_dump = f.read().strip().split()

pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
matches = [pattern.findall(dump) for dump in memory_dump]
print(sum(int(a[0]) * int(a[1]) for i in matches for a in i))
