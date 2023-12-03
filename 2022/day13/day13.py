filename = 'test-data.txt'

with open(filename, 'r') as file:
    data = [pair.split('\n') for pair in file.read().strip().split('\n\n')]

indexes = []
for i, d in enumerate(data, start=1):
    left, right = d
    left_len, right_len = len(left), len(right)

    if left_len < right_len:
        indexes.append(i)
        continue