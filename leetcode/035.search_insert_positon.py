class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # another binary search
        l = len(nums)
        if l == 0:
            return 0
        start = 0
        end = l-1
        while end>start:
            mid = (end+start)/2
            num = nums[mid]
            if target == num:
                return mid
            if target > num:
                start = mid+1
            else:
                end = mid-1
        num = nums[start]
        if target <= num:
            return start
        return start+1

        # binary search, O(log(n))
        l = len(nums)
        if l == 0:
            return 0
        start = 0
        end = l-1
        while end-start>1:
            mid = (end+start)/2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                start = mid
            else:
                end = mid
        if target <= nums[start]:
            return start
        if target <= nums[end]:
            return end
        return end+1
        
        
        # first version, O(n)
        l = len(nums)
        if l == 0:
            return 0
        for i in xrange(l):
            if target <= nums[i]:
                return i
        return i+1

s = Solution()
nums = [1, 3, 5, 7]
target = 9
print s.searchInsert(nums, target)
