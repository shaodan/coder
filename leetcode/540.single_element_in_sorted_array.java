import java.util.Arrays;

class Solution {

    public static void main(String[] args) {
        int[] nums = {1, 1, 2, 2, 3, 4, 4};
        Solution s = new Solution();
        int single = s.singleNonDuplicate(nums);
        System.out.println(Arrays.toString(nums));
        System.out.println(single);
    }

    public int singleNonDuplicate(int[] nums) {
        if (nums.length == 0)
            return 0;
        int left=0,right=nums.length-1,mid,len;
        while (left<right) {
            len = (right-left)/2;
            mid = (left+right)/2;
            if ((len&1)==0) {
                if (nums[mid-1] == nums[mid])
                    right = mid-2;
                else if (nums[mid+1] == nums[mid])
                    left = mid+2;
                else {
                    left = mid;
                    break;
                }
            } else {
                if (nums[mid-1] == nums[mid])
                    left = mid+1;
                else
                    right = mid-1;
            }
        }
        return nums[left];
    }
}
