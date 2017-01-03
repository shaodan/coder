/*
 * @lc app=leetcode id=22 lang=rust
 *
 * [22] Generate Parentheses
 *
 * https://leetcode.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (54.38%)
 * Total Accepted:    396.4K
 * Total Submissions: 693.3K
 * Testcase Example:  '3'
 *
 *
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 *
 *
 *
 * For example, given n = 3, a solution set is:
 *
 *
 * [
 * ⁠ "((()))",
 * ⁠ "(()())",
 * ⁠ "(())()",
 * ⁠ "()(())",
 * ⁠ "()()()"
 * ]
 *
 */
impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        if n == 1 {
            return vec!["()".to_string()];
        }
        // Backtracking Aglorithm
        let mut res = Vec::new();
        // recursion implement
        backtrack(&mut res, "", n, n);
        res
    }
}

fn backtrack(res: &mut Vec<String>, prefix: &str, left: i32, right: i32) {
    if left > right || left < 0 {
        return
    }
    if right == 0 {
        res.push(prefix.to_string())
    }
    backtrack(res, &(format!("{})", prefix)), left, right-1);
    backtrack(res, &(format!("{}(", prefix)), left-1, right);
}
