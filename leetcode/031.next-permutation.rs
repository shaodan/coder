/*
 * @lc app=leetcode id=31 lang=rust
 *
 * [31] Next Permutation
 *
 * https://leetcode.com/problems/next-permutation/description/
 *
 * algorithms
 * Medium (31.15%)
 * Total Accepted:    279.7K
 * Total Submissions: 897.1K
 * Testcase Example:  '[1,2,3]'
 *
 * Implement next permutation, which rearranges numbers into the
 * lexicographically next greater permutation of numbers. *
 * If such arrangement is not possible, it must rearrange it as the lowest
 * possible order (ie, sorted in ascending order).
 *
 * The replacement must be in-place and use only constant extra memory.
 *
 * Here are some examples. Inputs are in the left-hand column and its
 * corresponding outputs are in the right-hand column.
 *
 * 1,2,3 → 1,3,2
 * 3,2,1 → 1,2,3
 * 1,1,5 → 1,5,1
 *
 */

impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        let n = nums.len();
        if n < 2 {
            return;
        }
        // step 1
        let mut i = n - 2;
        while i > 0 && nums[i] >= nums[i+1] {
            i -= 1;
        }
        // usize overflow < 0
        if i == 0 && nums[0] >= nums[1] {
            nums.reverse();
            return;
        }
        let first = i;
        // step 2
        i = n - 1;
        while nums[i] <= nums[first] {
            i -= 1;
        }
        nums.swap(first, i);
        (nums[(first+1)..]).reverse();
    }
}
