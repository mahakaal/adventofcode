import re

with open('puzzle.txt', 'r') as file:
    pattern = re.compile(r'(\d+)-(\d+)')
    lines = [line for line in file.read().split(',') if line.strip()]
    input = []
    for line in lines:
        matches = pattern.findall(line)
        if matches:
            input.append((int(matches[0][0]), int(matches[0][1])))


def find_wrong_ids(intervals: [(int, int)], repeated: bool) -> int:
    invalid_patterns = set()
    invalid_numbers = set()

    pattern = r'(.+?)\1'
    if repeated:
        pattern += '+'

    pattern += '$'
    repeating_pattern = re.compile(pattern)

    for interval in intervals:
        for num in range(interval[0], interval[1] + 1):
            repeats = repeating_pattern.match(str(num))
            if repeats:
                if repeated:
                    invalid_numbers.add(num)
                elif not repeats.group(1) in invalid_patterns:
                    invalid_patterns.add(repeats.group(1))
                    invalid_numbers.add(num)

    return sum(invalid_numbers)


print('Part 1', find_wrong_ids(input, False))
print('Part 2', find_wrong_ids(input, True))
