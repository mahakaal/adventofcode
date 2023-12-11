package main

import (
	"fmt"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	lines := ReadFile("puzzle.txt")
	re := regexp.MustCompile("\\d+")
	games := make([][]int, len(lines))

	for i, line := range lines {
		found := re.FindAllString(line, -1)
		for j := 0; j < len(found); j++ {
			games[i] = append(games[i], GetNumber(found[j]))
		}
	}

	Part1(games)
	Part2(games)
}

func ReadFile(filename string) []string {
	file, err := os.ReadFile(filename)
	if err != nil {
		return nil
	}

	return strings.Split(strings.TrimSpace(string(file)), "\n")
}

func GetNumber(number string) (n int) {
	if v, err := strconv.Atoi(number); err == nil {
		n = v
	}

	return n
}

// GetWinningCases to get winning cases it must satisfied be the following inequality
// x(T-x) > D
// where T = total time, D = distance, x = button's optimal pressing time
// we can brute force by looping or use math to find out minimum and maximum points for the above inequality
// which becomes -x^2 + Tx - D > 0 -> x^2 - Tx + D < 0 -> x^2 - Tx + D = 0
// and apply quadratic formula. If the two solutions are not integer then floor the lesser and ceil the greater; otherwise add 1 to lesser and subtract to the other;
// Calculating winning cases is just maximum - minimum + 1
func GetWinningCases(time int, distance int) int {
	delta := math.Sqrt(float64(time*time - (4 * distance)))
	minvalue := (float64(time) - delta) / 2
	maxvalue := (float64(time) + delta) / 2

	if minvalue-float64(int(minvalue)) == 0 {
		minvalue += 1
	} else {
		minvalue = math.Ceil(minvalue)
	}

	if maxvalue-float64(int(maxvalue)) == 0 {
		maxvalue -= 1
	} else {
		maxvalue = math.Floor(maxvalue)
	}

	return int(maxvalue-minvalue) + 1
}

func Part1(records [][]int) {
	var cases []int
	total := 1
	for i := 0; i < len(records[0]); i++ {
		t := GetWinningCases(records[0][i], records[1][i])
		cases = append(cases, t)
		total *= t
	}

	fmt.Println(cases, total)
}

func Part2(records [][]int) {
	r := make([]string, len(records))
	for i, v := range records {
		str := ""
		for j := 0; j < len(v); j++ {
			str += fmt.Sprintf("%d", v[j])
		}
		r[i] = str
	}

	time, distance := GetNumber(r[0]), GetNumber(r[1])

	fmt.Println(GetWinningCases(time, distance))
}
