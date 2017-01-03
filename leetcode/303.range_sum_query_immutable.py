class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        l = len(nums)
        sums = [0]*(l+1)
        total = 0
        for i in range(l):
            total += nums[i]
            sums[i+1] = total
        self.sums = sums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1] - self.sums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

funs = ["NumArray","sumRange","sumRange","sumRange"]
args = [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]
