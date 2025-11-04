package main

import "fmt"

func isPalindrome(x int) bool {
	// 負の数は回文にならない
	if x < 0 {
		return false
	}

	original := x
	reversed := 0

	for x > 0 {
		dight := x % 10
		reversed = reversed * 10 + dight
		x /= 10
	}

	return original == reversed
}

func main() {
	fmt.Println(isPalindrome(121))
}