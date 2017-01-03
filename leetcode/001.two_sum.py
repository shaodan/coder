def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        loc = {y:x for x,y in enumerate(nums)}
        res = [0,0]
        for i, num in enumerate(nums):
            if (target-num) in loc:
                j = loc[target-num]
                if i!=j:
                    res[0] = i
                    res[1] = j
                    return res


nums = [3,2,4]
target = 7

print twoSum(nums, target)
