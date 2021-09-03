/*
Given a signed 32-bit integer x, return x
with its digits reversed. If reversing x causes the value to
go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Example 1:
    Input: x = 123
    Output: 321
Example 2:
    Input: x = -123
    Output: -321
Example 3:
    Input: x = 120
    Output: 21

Example 4:
    Input: x = 0
    Output: 0
*/

package main

import (
	"fmt"
)

func main() {
	data := -123
	fmt.Println(reverseIntegerSolution(data))

}

func reverseIntegerSolution(data int) int {
	var suma int = 0
	for data != 0 {
		suma = suma*10 + data%10
		data /= 10
	}
	return suma
}
