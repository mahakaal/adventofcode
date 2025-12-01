with open('puzzle.txt') as f:
    lines = [
        int(line.strip().replace('L', '-').replace('R', ''))
        for line in f if line.strip()
    ]

counter = 50
part1 = 0
part2 = 0
for value in lines:
    old = counter
    passes = 0
    intermediate = counter + value


    ### check for increment
    ### if positive we need to check how many times we crossed 0 from the previous iteration
    ### -1 ensures we don't double count if we arrive at a 100's multiple
    ### if negative means we decremented, just flip the substraction and remove the -1 because of the floor (// 100)
    ### max to ensure 0 passes when no cross is done
    if value > 0:
        passes = max(0, (intermediate - 1) // 100 - (old - 1) // 100)
    elif value < 0:
        passes = max(0, (old) // 100 - (intermediate) // 100)
    else:
        passes = 0

    counter = intermediate % 100
    part1 += (counter == 0)
    part2 += passes

print("part 1 %d part 2 %d" % (part1, part2))