def read_file(file_name: str) -> [int]:
    with open(file_name, 'r') as file:
        return [int(i) for i in file.read().strip().split(',')]


def part1(data: [int]) -> int:
    for day in range(80):
        zeroes = sum(i == 0 for i in data)
        data = [i - 1 if i > 0 else 6 for i in data] + ([8] * zeroes)
    return len(data)


def part2(data: [int], days: int) -> int:
    fish_per_lifespan: [] = [data.count(span) for span in range(9)]
    for day in range(days):
        zeroes = fish_per_lifespan[0]  # count 0 life span ones
        fish_per_lifespan[:-1] = fish_per_lifespan[1:]  # decrement fish with lifespan 1
        fish_per_lifespan[6] += zeroes  # respawn 0 lifespan fishes
        fish_per_lifespan[8] = zeroes  # new born
    return sum(fish_per_lifespan)


fishes: [] = read_file("puzzle.txt")
print(part1(fishes))
print(part2(fishes, 256))
