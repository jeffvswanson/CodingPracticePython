package main

import "fmt"

func main() {
	rem := 7.24
	fmt.Printf("%T\n", rem)
	fmt.Printf("%T\n", int(rem))

	var val interface{} = 7
	fmt.Printf("%T\n", rem)
	fmt.Printf("%T\n", int(val)) //purposeful error to show an interface cannot
	// be cast, but has to have asserstion.
	// correct = val.(int)
}
