def read_file(file_name):
    with open(file_name, "r") as file:
        return [int(i) for i in file.read().strip().split(',')]


def gauss_sum(start, end):
    diff = abs(start-end)
    return (diff/2) * (diff + 1)


data = read_file("puzzle.txt")
data.sort()
positions = [(i, sum(abs(i - y) for y in data)) for i in range(data[0], data[-1])]
print(min(positions, key=lambda x: x[1]))

positions = [(i, sum(gauss_sum(i, y) for y in data)) for i in range(data[0], data[-1])]
print(min(positions, key=lambda x: x[1]))

"""
Explanation for part two
look for instance at 16 -> 5 fuel consumption 66 while the distance is just 11, write down the progression
16 15 14 13 12 11 10 09 08 07 06 05
00 01 02 03 04 05 06 07 08 09 10 11 = 66 (sum the progression)

From an arithmetic view there is only one way that a distance of 11 gets to 66: 11 * 6 but what is 6?
Count the progression from start to end: it's distance + 1.
To get to 66 from 12 surely you multiply by 5.5, which is exactly the mean for 11, the original distance.
Write down the formula:
(distance/2) * (distance + 1) this oddly resembles Gauss Sum (n(n+1)/2) when n is odd

Let's test for the second example:
1 -> 5 fuel consumption 10, seems the double
01 02 03 04 05
00 01 02 03 04 = 10 aply the formula

distance is 4 so
(4/3)*(4+1) = 10

Eureka! 
"""

"""
--- Day 7: The Treachery of Whales ---

A giant whale has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!

Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you! They seem to be preparing to blast a hole in the ocean floor; sensors indicate a massive underground cave system just beyond where they're aiming!

The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your submarine to get through. However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?

There's one major catch - crab submarines can only move horizontally.

You quickly make a list of the horizontal position of each crab (your puzzle input). Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.

For example, consider the following horizontal positions:

16,1,2,0,4,2,7,1,2,14

This means there's a crab with horizontal position 16, a crab with horizontal position 1, and so on.

Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position 2:

    Move from 16 to 2: 14 fuel
    Move from 1 to 2: 1 fuel
    Move from 2 to 2: 0 fuel
    Move from 0 to 2: 2 fuel
    Move from 4 to 2: 2 fuel
    Move from 2 to 2: 0 fuel
    Move from 7 to 2: 5 fuel
    Move from 1 to 2: 1 fuel
    Move from 2 to 2: 0 fuel
    Move from 14 to 2: 12 fuel

This costs a total of 37 fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).

Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?

Your puzzle answer was 335330.
--- Part Two ---

The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?

As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes 5:

    Move from 16 to 5: 66 fuel
    Move from 1 to 5: 10 fuel
    Move from 2 to 5: 6 fuel
    Move from 0 to 5: 15 fuel
    Move from 4 to 5: 1 fuel
    Move from 2 to 5: 6 fuel
    Move from 7 to 5: 3 fuel
    Move from 1 to 5: 10 fuel
    Move from 2 to 5: 6 fuel
    Move from 14 to 5: 45 fuel

This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 fuel instead.

Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?

Your puzzle answer was 92439766.

Both parts of this puzzle are complete! They provide two gold stars: **
"""