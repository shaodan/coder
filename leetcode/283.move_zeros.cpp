class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int size = nums.size();
        int i,j=-1,n;
        for (i=0;i<size;i++) {
            if (nums[i]==0) {
                j=i;
                break;
            }
        }
        for (;i<size;i++) {
            n = nums[i];
            if (n!=0) {
                nums[j++] = n;
                nums[i] = 0;
            }
        }
        
    }
};
