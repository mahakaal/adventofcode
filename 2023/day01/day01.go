package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strings"
)

var digits = map[string]int{
	"one":   1,
	"two":   2,
	"three": 3,
	"four":  4,
	"five":  5,
	"six":   6,
	"seven": 7,
	"eight": 8,
	"nine":  9,
	"1":     1,
	"2":     2,
	"3":     3,
	"4":     4,
	"5":     5,
	"6":     6,
	"7":     7,
	"8":     8,
	"9":     9,
}

func main() {
	puzzle := "/Users/sukhdevmohan/Documents/workspace/go/adventofcode/2023/day01/puzzle.txt"
	// puzzle := "/Users/sukhdevmohan/Documents/workspace/go/adventofcode/2023/day01/example.txt"
	// puzzle := "/Users/sukhdevmohan/Documents/workspace/go/adventofcode/2023/day01/example2.txt"

	file, err := readLines(puzzle)
	if err != nil {
		log.Fatal(err)
		return
	}

	lines := strings.Split(string(file), "\n")
	fmt.Printf("Part 1 Total is : %d\n", part1(lines))
	fmt.Printf("Part 2 Total is : %d\n", part2(lines))
}

func readLines(filename string) (file []byte, err error) {
	return os.ReadFile(filename)
}

func part1(lines []string) int {
	total := 0
	re := regexp.MustCompile("\\d")
	for _, line := range lines {
		found := re.FindAllString(line, -1)
		if found == nil {
			continue
		}

		if first, ok := digits[found[0]]; ok {
			total += first * 10
		}

		if last, ok := digits[found[len(found)-1]]; ok {
			total += last
		}

	}

	return total
}

func part2(lines []string) int {
	total := 0
	re := regexp.MustCompile("\\d|one|two|three|four|five|six|seven|eight|nine")

	for _, line := range lines {
		var current []string

		for i := range line {
			found := re.FindString(line[i:])
			if found == "" {
				continue
			}

			current = append(current, found)
		}

		if first, ok := digits[current[0]]; ok {
			total += first * 10
		}

		if last, ok := digits[current[len(current)-1]]; ok {
			total += last
		}
	}

	return total
}
