/*
 * [461] Hamming Distance
 *
 * https://leetcode.com/graphql
 *
 * algorithms
 * Easy (69.67%)
 * Total Accepted:    121K
 * Total Submissions: 173.6K
 * Testcase Example:  '1\n4'
 *
 * The Hamming distance between two integers is the number of positions at
 * which the corresponding bits are different.
 * 
 * Given two integers x and y, calculate the Hamming distance.
 * 
 * Note:
 * 0 ≤ x, y < 231.
 * 
 * 
 * Example:
 * 
 * Input: x = 1, y = 4
 * 
 * Output: 2
 * 
 * Explanation:
 * 1   (0 0 0 1)
 * 4   (0 1 0 0)
 * ⁠      ↑   ↑
 * 
 * The above arrows point to positions where the corresponding bits are
 * different.
 * 
 * 
 */
package main

import "fmt"

func hammingDistance(x int, y int) int {
    var i int
    x ^= y
    for i=0;x>0;i++ {
        x &= x-1
    }
    return i
}

func main() {
    fmt.Println(1, 4, hammingDistance(1, 4))
}