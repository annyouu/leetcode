package main

import (
	"fmt"
)

func isValid(s string) bool {
	stack := []rune{}

	mapping := map[rune]rune{
		')':'(',
		'}':'{',
		']':'[',
	}

	for _, char := range s {
		if char == '(' || char == '{' || char == '[' {
			stack = append(stack, char)
		} else if (char == ')' || char == '}' || char == ']') {
			if len(stack) == 0 {
				return false
			}

			top := stack[len(stack) - 1]
			stack = stack[:len(stack) - 1]

			if mapping[char] != top {
				return false
			}
		}
	}
	return len(stack) == 0
}


func main() {
	input := "()"
	ans := isValid(input)

	fmt.Println(ans)
}

