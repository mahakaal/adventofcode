import copy
import re


def read_file(filename: str) -> ([str], [()]):
    with open(filename, 'r') as file:
        file_data = file.read()
        definition, moves = file_data.split('\n\n')
        containers = []

        for line in definition.split('\n')[: -1]:
            replace = ' [0]'

            if line[0] == ' ':
                replace = '[0] '

            containers.append(line.replace('    ', replace).split())

        max_len = max([len(line) for line in containers])

        for line in containers:
            t = max_len - len(line)
            if t > 0:
                line += ['[0]'] * t
        t = []

        for i in range(len(containers[0])):
            y = []
            for j in range(len(containers)):
                if containers[j][i] != '[0]':
                    y.append(containers[j][i])
            t.append(y)

        pattern = r'^move (\d+) from (\d+) to (\d+)$'

        # [(qty, src, dst)...]
        instruction_list = [list(map(lambda x: int(x), re.findall(pattern, line)[0])) for line in
                            moves.strip().split('\n')]

        return t, instruction_list


def day5() -> (str, str):
    file_name = 'puzzle.txt'
    stack_to_move, instructions_to_follow = read_file(file_name)

    def rearrange(stack: [[str]], instructions: [[str]], reverse: bool) -> [[str]]:
        for instruction in instructions:
            qty, src, dst = instruction
            t = stack[src - 1][:qty]

            if reverse:
                t.reverse()

            stack[dst - 1] = t + stack[dst - 1]
            stack[src - 1] = stack[src - 1][qty:]

        return ''.join([line[0] for line in stack]).replace('[', '').replace(']', '')

    part1 = rearrange(copy.deepcopy(stack_to_move), instructions_to_follow, True)
    part2 = rearrange(copy.deepcopy(stack_to_move), instructions_to_follow, False)

    return part1, part2


if __name__ == "__main__":
    print("Part 1: %s, Part 2: %s" % day5())
