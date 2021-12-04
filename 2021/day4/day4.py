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

"""
--- Day 4: Giant Squid ---

You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

Your puzzle answer was 72770.
--- Part Two ---

On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?

Your puzzle answer was 13912.

Both parts of this puzzle are complete! They provide two gold stars: **
"""