package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"slices"
	"strconv"
	"strings"
	"sync"
)

type Info struct {
	dest   int
	src    int
	length int
}
type Almanac map[string][]Info

func main() {
	lines := ReadLines("puzzle.txt")
	seeds, almanac := Initialize(lines)
	Part1(seeds, almanac)
	Part2(seeds, almanac)
}

func ReadLines(filename string) []string {
	file, err := os.ReadFile(filename)
	if err != nil {
		return nil
	}

	return strings.Split(strings.TrimSpace(string(file)), "\n\n")
}

func GetNumber(stringNumber string) (k int) {
	if v, err := strconv.Atoi(stringNumber); err == nil {
		k = v
	}

	return
}

func Initialize(lines []string) (seeds []int, almanac Almanac) {
	seedsRE := regexp.MustCompile("seeds:\\s((\\d+|\\s)+)")
	seedString := seedsRE.FindAllStringSubmatch(lines[0], -1)
	instructionNameRE := regexp.MustCompile("^\\s*([a-z\\-]+)\\s*map:")
	instructionRangesRE := regexp.MustCompile("^\\s*(\\d+)\\s(\\d+)\\s(\\d+)\\s*")
	if seedString == nil {
		log.Fatal("Seeds not captured")
	}

	almanac = Almanac{}
	for _, k := range strings.Split(seedString[0][1], " ") {
		seeds = append(seeds, GetNumber(k))
	}

	for _, line := range lines[1:] {
		instructions := strings.Split(line, "\n")
		name := instructionNameRE.FindAllStringSubmatch(instructions[0], -1)[0][1]

		for _, r := range instructions[1:] {
			result := instructionRangesRE.FindAllStringSubmatch(r, -1)
			info := Info{dest: GetNumber(result[0][1]), src: GetNumber(result[0][2]), length: GetNumber(result[0][3])}

			switch name {
			case "seed-to-soil":
				almanac["seedSoil"] = append(almanac["seedSoil"], info)
				break
			case "soil-to-fertilizer":
				almanac["soilFertilizer"] = append(almanac["soilFertilizer"], info)
				break
			case "fertilizer-to-water":
				almanac["fertilizerWater"] = append(almanac["fertilizerWater"], info)
				break
			case "water-to-light":
				almanac["waterLight"] = append(almanac["waterLight"], info)
				break
			case "light-to-temperature":
				almanac["lightTemperature"] = append(almanac["lightTemperature"], info)
				break
			case "temperature-to-humidity":
				almanac["temperatureHumidity"] = append(almanac["temperatureHumidity"], info)
				break
			case "humidity-to-location":
				almanac["humidityLocation"] = append(almanac["humidityLocation"], info)
				break
			default:
				log.Fatal("Not a case")
			}
		}
	}

	return
}

func GetNextMapping(value int, almanac Almanac, nextMap string) int {
	if v, ok := almanac[nextMap]; ok {
		for _, info := range v {
			if info.src <= value && value <= info.src+info.length {
				return info.dest + (value - info.src)
			}
		}
	}

	return value
}

func GetLocation(seed int, almanac Almanac) int {
	if soil := GetNextMapping(seed, almanac, "seedSoil"); soil >= 0 {
		if fertilizer := GetNextMapping(soil, almanac, "soilFertilizer"); fertilizer >= 0 {
			if water := GetNextMapping(fertilizer, almanac, "fertilizerWater"); water >= 0 {
				if light := GetNextMapping(water, almanac, "waterLight"); light >= 0 {
					if temperature := GetNextMapping(light, almanac, "lightTemperature"); temperature >= 0 {
						if humidity := GetNextMapping(temperature, almanac, "temperatureHumidity"); humidity >= 0 {
							if location := GetNextMapping(humidity, almanac, "humidityLocation"); location >= 0 {
								return location
							}
						}
					}
				}
			}
		}
	}

	return -1
}

func Part1(seeds []int, almanac Almanac) {
	var locations []int

	for _, seed := range seeds {
		locations = append(locations, GetLocation(seed, almanac))
	}

	fmt.Println("Part 1", slices.Min(locations))
}

func EvaluateRange(start int, length int, almanac Almanac, ch chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	var locations []int
	for i := start; i < start+length; i++ {
		if location := GetLocation(i, almanac); location > 0 {
			locations = append(locations, GetLocation(i, almanac))
		}
	}

	ch <- slices.Min(locations)
}

func Part2(seeds []int, almanac Almanac) {
	var locations []int
	channel := make(chan int, len(seeds))
	var wg sync.WaitGroup
	for i := 0; i < len(seeds); i += 2 {
		wg.Add(1)
		go EvaluateRange(seeds[i], seeds[i+1], almanac, channel, &wg)
	}
	wg.Wait()
	close(channel)

	for i := range channel {
		locations = append(locations, i)
	}

	fmt.Println("Part 2", slices.Min(locations))
}
