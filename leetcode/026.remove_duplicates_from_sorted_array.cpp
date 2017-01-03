class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int length = nums.size();
        int newLength = length;
        if (length<2) {
            return length;
        }
        int n;
        int prev = nums[0]-1;
        for (int i=0,j=0;i<length;i++) {
            n = nums[i];
            if (prev!=n) {
                if (i!=j) {
                    nums[j] = n;
                }
                j++;
                prev = n;
            } else {
                newLength--;
            }
        }
        return newLength;
    }
};
