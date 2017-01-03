/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int* result = NULL;
    int i=digitsSize-1,j;
    if (digits[i]==9) {
        do {
            i--;
        } while(i>=0 && digits[i]==9);
        if (i<0) {
            *returnSize = digitsSize+1;
            result = (int*)malloc(sizeof(int)*(*returnSize));
            for (i=digitsSize;i>0;i--) {
                result[i] = 0;
            }
            result[0] = 1;
        } else {
            *returnSize = digitsSize;
            result = (int*)malloc(sizeof(int)*(*returnSize));
            for (j=digitsSize-1;j>i;j--) {
                result[j] = 0;
            }
            result[i] = digits[i]+1;
            for (i--;i>=0;i--) {
                result[i] = digits[i];
            }
        }
    } else {
        *returnSize = digitsSize;
        result = (int*)malloc(sizeof(int)*(*returnSize));
        result[i] = digits[i]+1;
        for (i--;i>=0;i--) {
            result[i] = digits[i];
        }
    }
    return result;
}
