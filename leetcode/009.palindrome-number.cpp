/*
 * [9] Palindrome Number
 *
 * https://leetcode.com/problems/palindrome-number
 *
 * Easy (35.07%)
 * Total Accepted:    
 * Total Submissions: 
 * Testcase Example:  '-2147483648'
 *
 * Determine whether an integer is a palindrome. Do this without extra space.
 * 
 * click to show spoilers.
 * 
 * Some hints:
 * 
 * Could negative integers be palindromes? (ie, -1)
 * 
 * If you are thinking of converting the integer to string, note the
 * restriction of using extra space.
 * 
 * You could also try reversing an integer. However, if you have solved the
 * problem "Reverse Integer", you know that the reversed integer might
 * overflow. How would you handle such case?
 * 
 * There is a more generic way of solving this problem.
 * 
 * 
 */
#include <iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        int tmp=0;
        // if x == int32.minValue, -x == x then tmp < x, return false
        //x = x > 0 ? x : -x;
        // if x = 10 or 20 and soon
        if (x < 0 || (x!=0&&x%10==0)) return false; // ???? test cases show tha negative numbers are NOT PN
        //cout << x << endl;
        while (tmp < x) {
            tmp = tmp*10 + x%10;
            x /= 10;
            //cout << tmp << " " << x <<endl;
        }
        //cout << tmp << " " << x <<endl;
        //if (tmp == x || tmp/10 == x)
        //    return true;
        //return false; 
        // simplify return logic
        return (tmp == x || tmp/10 == x);
    }
};


int main() {
    Solution s;
    int a[] = {-2147447412, -2147483648, 1111111118, -2111111112, -2147483647, 10, 121, 0, -1, 12};
    int l = sizeof(a) /sizeof(a[0]);
    for (int i=0 ; i < l ; i++) {
        cout << a[i ]<< " : " << s.isPalindrome(a[i]) << endl;
    }
    return 0;
}
