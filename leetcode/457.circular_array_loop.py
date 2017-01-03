def circularArrayLoop(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    if n < 2:
        return False
    for i in xrange(n):
        s = nums[i]
        if s == 0:
            continue
        c = 0
        k = i
        p = (s>0)
        while c < n:
            s = nums[k]
            k_t = (k+s)%n
            if k_t==k or (p^(s>0)):
                break
            k = k_t
            c += 1
        if c>=n:
            return True
        p = nums[i]>0
        k = i
        while 1:
            s = nums[i]
            k = (i+s)%n
            if k==i or (p^(s>0)):
                break
            nums[k] = 0
            i = k
    return False

# nums = [2, -1, 1, 2, 2]
# nums = [-2, 1, -1, -2, -2]
# nums = [3,1,2]
nums = [-1, 2]
print circularArrayLoop(nums)

