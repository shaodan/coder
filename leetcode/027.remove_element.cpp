class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int length = nums.size();
        int i=0,j=length-1;
        for (;i<=j;i++) {
            if (nums[i]==val) {
                length--;
                for (;j>i;j--) {
                    if (nums[j]!=val) {
                        nums[i] = nums[j--];
                        break;
                    }
                    length--;
                }
            }
        }
        return length;
    }
};
