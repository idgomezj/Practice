package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	prueba := []int{4, 2, 3, 1, 5}
	fmt.Println(miniMaxSum(prueba))
}

func miniMaxSum(arr []int) string {

	for _, s := range arr {
		if s < 1 || float64(s) > math.Pow(10, 9) {
			return ""
		}
	}
	sort.Ints(arr)
	min := 0
	max := 0

	for _, i := range arr[0:4] {
		min += i
	}
	for _, i := range arr[len(arr)-4 : len(arr)] {
		max += i
	}

	return fmt.Sprint(min, max, "")
}
