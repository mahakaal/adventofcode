import re

with open("puzzle.txt") as f:
    memory_dump = f.read().strip().split('\n')

pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
matches = [pattern.findall(line) for line in memory_dump]
sums = sum(int(a[0]) * int(a[1]) for i in matches for a in i)
print('part 1: ', sums)

extended_pattern = re.compile(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)')
sums = 0
do_sum = True
for line in memory_dump:
    for i in extended_pattern.finditer(line):
        match i[0]:
            case 'do()':
                do_sum = True
            case 'don\'t()':
                do_sum = False
            case _:
                if do_sum:
                    sums += int(i[1]) * int(i[2])

print('part 2: ', sums)