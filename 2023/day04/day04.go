package main

import (
	"fmt"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Card struct {
	number int
	won    int
	copies int
}

type Storage struct {
	cards []Card
}

func (storage *Storage) addCard(card Card) []Card {
	storage.cards = append(storage.cards, card)

	return storage.cards
}

func main() {
	lines := readLines("puzzle.txt")
	cards := new(Storage)
	part1(lines, cards)
	//prettyPrint(cards)
	part2(cards, len(lines))
}

func readLines(filename string) []string {
	file, err := os.ReadFile(filename)
	if err != nil {
		return nil
	}

	return strings.Split(strings.TrimSpace(string(file)), "\n")
}

func part1(lines []string, storage *Storage) {
	re := regexp.MustCompile("Card\\s+(\\d+):\\s+(.*)\\s+\\|\\s+(.*)\\n?")
	total := 0

	for _, line := range lines {
		found := re.FindAllStringSubmatch(line, -1)
		if found == nil {
			continue
		}

		var cardNum int
		if v, err := strconv.Atoi(found[0][1]); err == nil {
			cardNum = v
		}

		card := Card{number: cardNum, won: 0, copies: 1}
		numbers := strings.TrimSpace(found[0][3])
		var winning []string

		for _, v := range strings.Split(found[0][2], " ") {
			if v := strings.TrimSpace(v); v != "" {
				winning = append(winning, v)
			}
		}

		t := 0
		for _, winner := range winning {
			for _, num := range strings.Split(numbers, " ") {
				if num == winner {
					t++
				}
			}
		}

		if t > 0 {
			total += int(math.Pow(float64(2), float64(t-1)))
			card.won = t
		}

		storage.addCard(card)
	}

	fmt.Println("Part 1 answer:", total)
}

func part2(wonCards *Storage, lines int) {
	total := 0
	for _, card := range wonCards.cards {
		for j := card.number; j < card.number+card.won+1 && j-1 < lines; j++ {
			wonCards.cards[j-1].copies += card.copies
		}
		total += card.copies
	}

	fmt.Println("Part 2 answer:", total)
}

func generateNextValues(start int, end int, limit int) []int {
	var sequence []int
	for i := start + 1; i < start+end && i-1 < limit; i++ {
		sequence = append(sequence, i)
	}

	return sequence
}

func prettyPrint(storage *Storage) {
	for _, v := range storage.cards {
		fmt.Println("CARD", v.number)
		fmt.Printf("\tWON:%d\n", v.won)
		fmt.Printf("\tCOPIES:%d\n", v.copies)
		fmt.Println("-----------------------")
	}

	fmt.Println("- END -")
}
