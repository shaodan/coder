/*
 * @lc app=leetcode id=807 lang=rust
 *
 * [807] Max Increase to Keep City Skyline
 *
 * https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
 *
 * algorithms
 * Medium (82.10%)
 * Total Accepted:    62.4K
 * Total Submissions: 76K
 * Testcase Example:  '[[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]'
 *
 * In a 2 dimensional array grid, each value grid[i][j] represents the height
 * of a building located there. We are allowed to increase the height of any
 * number of buildings, by any amount (the amounts can be different for
 * different buildings). Height 0 is considered to be a building as well. 
 *
 * At the end, the "skyline" when viewed from all four directions of the grid,
 * i.e. top, bottom, left, and right, must be the same as the skyline of the
 * original grid. A city's skyline is the outer contour of the rectangles
 * formed by all the buildings when viewed from a distance. See the following
 * example.
 *
 * What is the maximum total sum that the height of the buildings can be
 * increased?
 *
 *
 * Example:
 * Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
 * Output: 35
 * Explanation:
 * The grid is:
 * [ [3, 0, 8, 4],
 * ⁠ [2, 4, 5, 7],
 * ⁠ [9, 2, 6, 3],
 * ⁠ [0, 3, 1, 0] ]
 *
 * The skyline viewed from top or bottom is: [9, 4, 8, 7]
 * The skyline viewed from left or right is: [8, 7, 9, 3]
 *
 * The grid after increasing the height of buildings without affecting skylines
 * is:
 *
 * gridNew = [ [8, 4, 8, 7],
 * ⁠           [7, 4, 7, 7],
 * ⁠           [9, 4, 8, 7],
 * ⁠           [3, 3, 3, 3] ]
 *
 *
 *
 * Notes:
 *
 *
 * 1 < grid.length = grid[0].length <= 50.
 * All heights grid[i][j] are in the range [0, 100].
 * All buildings in grid[i][j] occupy the entire grid cell: that is, they are a
 * 1 x 1 x grid[i][j] rectangular prism.
 *
 *
 */
use std::cmp;

impl Solution {
    pub fn max_increase_keeping_skyline(grid: Vec<Vec<i32>>) -> i32 {
        let x = grid.len();
        let y = grid[0].len();
        let mut v;
        let mut skyline_row = vec![0; x];
        let mut skyline_column = vec![0; y];
        for i in 0..x {
            for j in 0..y {
                v = grid[i][j];
                if v > skyline_row[i] {
                    skyline_row[i] = v;
                }
                if v > skyline_column[j] {
                    skyline_column[j] = v;
                }
            }
        }
        let mut sum = 0;
        for i in 0..x {
            for j in 0..y {
                // upper limit
                v = cmp::min(skyline_row[i], skyline_column[j]);
                v = cmp::max(v, grid[i][j]);
                sum += v - grid[i][j];
            }
        }
        sum
    }
}
