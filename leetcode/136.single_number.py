# int singleNumber(int* nums, int numsSize) {
#     int i;
#     int res;
#     for (i=0;i<numsSize;i++) {
#         res ^= nums[i];
#     }
#     return res;
# }

def singleNumber(nums):
    res = 0
    for x in nums:
        res ^= x
    return res

input = range(100)*2 + [100] + range(101,200)*2

print singleNumber(input)
