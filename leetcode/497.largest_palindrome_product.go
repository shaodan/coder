package main

import "fmt"

func largestPalindrome(n int) int {
	if n == 1 {
		return 9
	}
	max_l := [...]int{9, 99, 999, 9999, 99999, 999999, 9999999, 99999999}
	max := max_l[n-1]
	min := max / 10

	for left := max - 1; left > min; left-- {
		prd := palindromfy(left)
		for i := int64(max); i*i >= prd; i-- {
			if prd%i == 0 {
				return int(prd % 1337)
			}
		}
	}
	return 0
}

func palindromfy(left int) int64 {
	var total int64 = int64(left)
	var right int = 0
	for ; left > 0; left /= 10 {
		total *= 10
		right = (right * 10) + (left % 10)
	}
	return total + int64(right)
}

func main() {
	a := largestPalindrome(3)
	fmt.Println(a)
}
