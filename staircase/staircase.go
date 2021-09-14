package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(solve(6))
}

func solve(n int) string {
	if n < 0 || n > 100 {
		return ""
	}
	resolve := strings.Repeat(" ", n-1) + "#"
	for i := 2; i < n+1; i++ {
		resolve += "\n" + strings.Repeat(" ", n-i) + strings.Repeat("#", i)
	}
	return resolve
}
