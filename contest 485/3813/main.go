package main

import (
	// "fmt"
)

func vowelConsonantScore(s string) int {
	v := 0
	c := 0

	for _, ch := range s {
		// 英字かどうか
		// ダメ 連続ではできない　if ('a' <= ch <= 'z') 
		if (ch >= 'a' && ch <= 'z') {
			// 母音判定
			if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
				v++
			} else {
				c++
			}
		}
	}

	if c == 0 {
		return 0
	} else {
		return v / c
	}
}