package main

// import "fmt"

func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)

	for i, num := range nums {
		diff := target - num
		// これについて(j, ok = seen[diff])という書き方ができるん？
		if j, ok := seen[diff]; ok {
			return []int{i, j}
		}
		// これってなんだっけ？
		seen[num] = i
	}
	// 何もなかったらnilを返すのってないとマズイの？
	return nil
}