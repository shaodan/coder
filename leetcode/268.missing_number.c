int missingNumber(int* nums, int numsSize) {
    int i;
    int k1=numsSize^(numsSize-1);
    int k2=nums[numsSize-1];
    for (i=numsSize-2;i>=0;i--) {
        k1 ^= i;
        k2 ^= nums[i];
    }
    return k1^k2;
}
