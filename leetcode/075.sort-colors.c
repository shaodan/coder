/*
 * @lc app=leetcode id=75 lang=c
 * [75] Sort Colors
 * https://leetcode.com/problems/sort-colors/description/
 *
 * algorithms
 * Medium (43.43%)
 * Total Accepted:    368.4K
 * Total Submissions: 846.1K
 * Testcase Example:  '[2,0,2,1,1,0]'
 *
 * Given an array with n objects colored red, white or blue, sort them in-place
 * so that objects of the same color are adjacent, with the colors in the order
 * red, white and blue.
 *
 * Here, we will use the integers 0, 1, and 2 to represent the color red,
 * white, and blue respectively.
 *
 * Note: You are not suppose to use the library's sort function for this
 * problem.
 *
 * Example:
 * Input: [2,0,2,1,1,0]
 * Output: [0,0,1,1,2,2]
 *
 * Follow up:
 * A rather straight forward solution is a two-pass algorithm using counting
 * sort.
 * First, iterate the array counting number of 0's, 1's, and 2's, then
 * overwrite array with total number of 0's, then 1's and followed by 2's.
 * Could you come up with a one-pass algorithm using only constant space?
 *
 */

// Solution 1: one-pass algorithm
void sortColors(int* nums, int numsSize){
    int j=0, k=numsSize-1;
    for (int i=0;i<=k;i++) {
        if (nums[i] == 0) {
            swap(nums, i, j++);
        } else if (nums[i] == 2) {
            swap(nums, i--, k--);
        }
    }
}

inline void swap(int* nums, int a, int b) {
    int temp = nums[a];
    nums[a] = nums[b];
    nums[b] = temp;
}

// Solution 1.1: one-pass algorithm
void sortColors(int* nums, int numsSize){
    if (numsSize < 2) {
        return;
    }
    int left=0,right=numsSize-1;
    int i=0;
    for (;i<=right;i++) {
        switch (nums[i]) {
            case 0:
                nums[i] = nums[left];
                nums[left++] = 0;
                break;
            case 2:
                for (;right>i;right--) {
                    if (nums[right] == 1) {
                        nums[i] = 1;
                        nums[right--] = 2;
                        break;
                    }
                    if (nums[right] == 0) {
                        nums[i] = nums[left];
                        nums[right--] = 2;
                        nums[left++] = 0;
                        break;
                    }
                }
                break;
        }
    }
}

// Solution 2: two-pass algorithm using counting sort
void sortColors_counting_sort(int* nums, int numsSize){
    if (numsSize < 2) {
        return;
    }
    int counts[] = {0, 0, 0};
    for (int i=numsSize-1;i>=0;i--) {
        counts[nums[i]] ++;
    }
    int j = 0;
    for (int k=counts[0]-1;k>=0;k--) {
        nums[j++] = 0;
    }
    for (int k=counts[1]-1;k>=0;k--) {
        nums[j++] = 1;
    }
    for (int k=counts[2]-1;k>=0;k--) {
        nums[j++] = 2;
    }
}

