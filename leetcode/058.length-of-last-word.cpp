/*
 * @lc app=leetcode id=58 lang=cpp
 *
 * [58] Length of Last Word
 *
 * https://leetcode.com/problems/length-of-last-word/description/
 *
 * algorithms
 * Easy (32.23%)
 * Total Accepted:    301.4K
 * Total Submissions: 932.9K
 * Testcase Example:  '"Hello World"'
 *
 * Given a string s consists of upper/lower-case alphabets and empty space
 * characters ' ', return the length of last word in the string.
 *
 * If the last word does not exist, return 0.
 *
 * Note: A word is defined as a character sequence consists of non-space
 * characters only.
 *
 * Example:
 * Input: "Hello World"
 * Output: 5
 *
 */
class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.size() - 1;
        for (;i>=0 && s[i] == ' ';--i) {}
        if (i < 0) {
            return 0;
        }
        int j = i - 1;
        for (;j>=0 && s[j] != ' ';--j) {}
        return i - j;
    }
};
