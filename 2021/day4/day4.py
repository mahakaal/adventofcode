import re
from copy import deepcopy
from typing import Tuple, List


def read_file(file_name: str) -> Tuple[List, List]:
    with open(file_name, "r") as file:
        bingo = list(map(lambda x: int(x), file.readline().strip().split(',')))
        charts = [[list(map(lambda x: int(x), re.split('\s+', row.strip()))) for row in chart.split("\n")]
                  for chart in file.read().strip().split("\n\n")]

        return bingo, charts


def mark_number(bingo_board: List, number: int):
    for row in bingo_board:
        if number in row:
            row[row.index(number)] = -1


def check_bingo(bingo_board: List) -> bool:
    transposed_bingo_board = list(zip(*bingo_board))
    for i in range(0, 5):
        if sum(bingo_board[i]) == -5 or sum(transposed_bingo_board[i]) == -5:
            return True

    return False


def day4(file_name: str) -> Tuple:
    bingo_numbers, boards = read_file(file_name)

    def part1(in_numbers: List, in_boards: List) -> Tuple:
        boards_copy = deepcopy(in_boards)
        is_bingo, winning_board = False, None
        for number in in_numbers:
            for i in range(0, len(boards_copy)):
                mark_number(boards_copy[i], number)

                if check_bingo(boards_copy[i]):
                    is_bingo = True
                    winning_board = boards_copy[i]
                    break

            if is_bingo:
                flat = [item for row in winning_board for item in row if item > 0]
                return sum(flat) * number, i

    def part2(in_numbers: List, in_boards: List) -> int:
        boards_copy = deepcopy(in_boards)

        while len(boards_copy) > 1:
            _, board = part1(in_numbers, boards_copy)
            del boards_copy[board]

        return part1(in_numbers, boards_copy)[0]

    return part1(bingo_numbers, boards)[0], part2(bingo_numbers, boards)


print("Part 1 %d, Part2: %d" % day4("puzzle.txt"))
