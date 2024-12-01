package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Hand struct {
	cards  string
	bid    int
	points int
}

type Game struct {
	hands []Hand
}

var strengths = map[string]int{
	"A": 13,
	"K": 12,
	"Q": 11,
	"J": 10,
	"T": 9,
	"9": 8,
	"8": 7,
	"7": 6,
	"6": 5,
	"5": 4,
	"4": 3,
	"3": 2,
	"2": 1,
}

func (game *Game) AddHand(hand Hand) []Hand {
	game.hands = append(game.hands, hand)

	return game.hands
}

func main() {
	lines := ReadFile("example.txt")
	game := new(Game)
	InitializeGame(game, lines)
	fmt.Println(game)
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

func InitializeGame(game *Game, lines []string) {
	re := regexp.MustCompile("^([AKQJT2-9]{5})\\s+(\\d+)$")
	for _, line := range lines {
		found := re.FindAllStringSubmatch(line, -1)
		game.hands = append(game.hands, Hand{cards: found[0][1], bid: GetNumber(found[0][2])})
	}
}

func GetRank(cards string) {
	total := 0
	for k, v := range strengths {
		if count := strings.Count(cards, k); count > 0 {
			total += v
		}
	}
}
