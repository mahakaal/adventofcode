package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Detail struct {
	dices int
	color string
}
type Set struct {
	details []Detail
}

type Game struct {
	id   int
	sets []Set
}

type GameBoard struct {
	games []Game
}

var configuration = map[string]int{
	"red":   12,
	"green": 13,
	"blue":  14,
}

func main() {
	filename := "puzzle.txt"
	lines := readLines(filename)

	if lines == nil {
		log.Fatal("Cannot read file")
		return
	}
	board := new(GameBoard)
	initializeGames(lines, board)
	part1(board)
	part2(board)
}

func (board *GameBoard) addGame(game Game) []Game {
	board.games = append(board.games, game)
	return board.games
}

func (game *Game) addSet(set Set) []Set {
	game.sets = append(game.sets, set)
	return game.sets
}

func (set *Set) addDetail(detail Detail) []Detail {
	set.details = append(set.details, detail)
	return set.details
}

func readLines(filename string) []string {
	file, err := os.ReadFile(filename)
	if err != nil {
		return nil
	}

	return strings.Split(strings.TrimSpace(string(file)), "\n")
}

func initializeGames(lines []string, board *GameBoard) {
	gameIdRE := regexp.MustCompile("Game (\\d+):")
	for _, line := range lines {
		found := gameIdRE.FindStringSubmatch(line)
		if len(found) == 0 {
			fmt.Println("Game ID not found for", line)
		}
		game := Game{}
		if v, err := strconv.Atoi(found[1]); err == nil {
			game.id = v
		}

		linePart := strings.Split(line, ":")
		for _, gameSet := range strings.Split(linePart[1], ";") {
			set := new(Set)
			for _, setDetail := range strings.Split(strings.TrimSpace(gameSet), ",") {
				detail := strings.Split(strings.TrimSpace(setDetail), " ")
				set.addDetail(Detail{dices: getNum(detail[0]), color: detail[1]})
			}

			game.addSet(*set)
		}

		board.addGame(game)
	}
}

func getNum(number string) int {
	if v, err := strconv.Atoi(number); err == nil {
		return v
	}

	return 0
}

func printBoard(board *GameBoard) {
	for _, game := range board.games {
		fmt.Println("Game ID", game.id)
		for i, set := range game.sets {
			fmt.Println("\tSet #", i+1)
			for j, detail := range set.details {
				fmt.Println("\t\tDetail #", j+1, detail)
			}
		}
	}
}

func part1(board *GameBoard) {
	idSum := 0
	for _, game := range board.games {
		invalid := false
		for i, set := range game.sets {
			for _, detail := range set.details {
				if detail.dices > configuration[detail.color] {
					invalid = true
					break
				}
			}

			if invalid {
				break
			} else if !invalid && i == len(game.sets)-1 {
				idSum += game.id
			}
		}
	}

	fmt.Println("Part 1 Answer", idSum)
}

func part2(board *GameBoard) {
	sum := 0
	for _, game := range board.games {
		red := 0
		blue := 0
		green := 0
		for _, set := range game.sets {
			for _, detail := range set.details {
				if detail.color == "red" && detail.dices > red {
					red = detail.dices
				}

				if detail.color == "blue" && detail.dices > blue {
					blue = detail.dices
				}

				if detail.color == "green" && detail.dices > green {
					green = detail.dices
				}
			}
		}

		sum += red * green * blue
	}

	fmt.Println("Part 2 Answer", sum)
}
