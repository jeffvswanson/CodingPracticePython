package main

import (
	"bufio"
	"fmt"
	"log"
	"net/http"
)

func main() {
	// Get the book, Sherlock Holmes.
	res, err := http.Get("http://www.gutenberg.org/cache/epub/1661/pg1661.txt")
	if err != nil {
		log.Fatal(err)
	}

	// Scan the page.
	// NewScanner takes a reader and a res.Body implements the reader interface
	// so it is a reader.
	scanner := bufio.NewScanner(res.Body)
	defer res.Body.Close()
	// Set the split function for the scanning operation.
	scanner.Split(bufio.ScanWords)
	// Create map with key of int
	// and a value of another map
	// with a key of string, which will be the word
	// and a value of int, which will be the number of times the word occurs
	buckets := make(map[int]map[string]int)
	// Create slices to hold words
	for i := 0; i < 12; i++ {
		buckets[i] = make(map[string]int)
	}
	// Loop over the words
	for scanner.Scan() {
		word := scanner.Text()
		n := hashBucket(word, 12)
		buckets[n][word]++
	}
	// Print the words in one of the buckets.
	for k, v := range buckets[6] {
		fmt.Println(v, " \t- ", k)
	}
}

func hashBucket(word string, buckets int) int {
	var sum int
	for _, v := range word {
		sum += int(v)
	}
	return sum % buckets
}
