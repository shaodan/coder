class Solution {
public:
    int titleToNumber(string s) {
        int size = s.size();
        int num = 0;
        for(int i=0; i<size; i++) {
            num = num*26+(s.at(i)-'A'+1);
        }
        return num;
    }
};
