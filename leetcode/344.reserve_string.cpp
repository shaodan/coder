#include <iostream>
using namespace std;


class Solution {
public:
    string reverseString(string s) {
        int last=s.length()-1;
        char t;
        for (int i=0;i<=last/2;i++) {
            t = s[i];
            s[i] = s[last-i];
            s[last-i] = t;
        }
        return s;
    }
    
    string reverseString2(string s) {
        int start = 0;
        int end=s.length()-1;
        char t;
        while(start < end)
            t = s[start];
            s[start] = s[end];
            s[end] = t;
            start++;
            end--;
        }
        return s;
    }
};

int main() {
	Solution sol;
    string s = "hello";
    cout << s <<endl;
    cout << sol.reverseString(s) <<endl;
}
