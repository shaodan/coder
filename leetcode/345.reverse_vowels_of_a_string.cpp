#include <iostream>
using namespace std;


class Solution {
public:
    inline void swap(string &s, int i, int j) {
        char c = s[i];
        s[i] = s[j];
        s[j] = c;
    }
    inline bool isVowel(char c) {
        return c=='a' || c=='e' || c=='i' || c=='o' || c=='u';
    }
    string reverseVowels(string s) {
        int len=s.length();
        int i=-1,j=len;
        while(true) {
            for (;i<j&&!isVowel(s[++i]);) {}
            for (;i<j&&!isVowel(s[--j]);) {}
            cout << i << ' ' << j<< endl;
            if (i<j) {
                swap(s, i, j);
                cout << s << endl;
            } else {
                break;
            }
        }
        return s;
    }
};

int main() {
	Solution sol;
    //string s = "hello";
    string s = "leetcode";
    cout << s <<endl;
    cout << sol.reverseVowels(s) <<endl;
}
