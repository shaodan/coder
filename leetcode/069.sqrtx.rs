/*
 * @lc app=leetcode id=69 lang=rust
 *
 * [69] Sqrt(x)
 *
 * https://leetcode.com/problems/sqrtx/description/
 *
 * algorithms
 * Easy (31.13%)
 * Total Accepted:    424.3K
 * Total Submissions: 1.3M
 * Testcase Example:  '4'
 *
 * Implement int sqrt(int x).
 *
 * Compute and return the square root of x, where x is guaranteed to be a
 * non-negative integer.
 *
 * Since the return type is an integer, the decimal digits are truncated and
 * only the integer part of the result is returned.
 *
 * Example 1:
 *
 *
 * Input: 4
 * Output: 2
 *
 *
 * Example 2:
 *
 *
 * Input: 8
 * Output: 2
 * Explanation: The square root of 8 is 2.82842..., and since
 * the decimal part is truncated, 2 is returned.
 *
 *
 */
impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        // Solution-1 Newton
        // newton(x)

        // Solution-2 Binary Search
        binary_search(x)
    }
}

fn newton(x: i32) -> i32 {
    let longx = x as i64;
    let mut r = longx;
    while r*r > longx {
        r = (r + longx/r) / 2;
    }
    r as i32
}

fn binary_search(x: i32) -> i32 {
    if x == 0 {
        return 0;
    }
    let mut left = 1;
    let mut right = x;
    let mut mid;
    let mut quo;

    while left < right-1 {
        mid = (left + right) / 2;
        quo = x / mid;
        if quo == mid {
            return mid;
        }
        if mid > quo  {
            right = mid;
        } else {
            left = mid;
        }
    }
    left
}
