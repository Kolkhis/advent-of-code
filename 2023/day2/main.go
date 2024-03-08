package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func read_file(path string) *os.File {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal("os.Open(): Problem opening file: ", err)
	}
	return file
}

func main() {
	var filename string = "./input.txt"
	file := read_file(filename)
	defer file.Close()
	// data, err := os.ReadFile(filename)  // Does not do what we need.
	fmt.Println(file)
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

}
