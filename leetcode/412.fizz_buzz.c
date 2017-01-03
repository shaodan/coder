#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char multiply3[] = "Fizz";
int size3 = 4;
char multiply5[] = "Buzz";
int size5 = 4;
char multiply15[] = "FizzBuzz";
int size15 = 8;


// char** fizzBuzz(int n, int* returnSize) {
//     char** result = (char**)malloc(sizeof(char*)*n);
//     int i,j,l;
//     returnSize[0] = 0;
//     for (i=1;i<n;i++) {
//         j = i+1;
//         returnSize[i] =returnSize[j/10]+1;
//     }
//     returnSize[0] = 1;
//     for (i=0;i<n;i++) {
//         j = i+1;
//         result[i] = (char*)malloc(sizeof(char)*l);
//     }
//     return result;
// }

char** fizzBuzzBad(int n, int* returnSize) {
    char** result = (char**)malloc(sizeof(char*)*n);
    int i,j,k,l,m;
    for (i=0;i<n;i++) {
        j = i+1;
        if (j%15==0) {
            result[i] = (char*)malloc(sizeof(char)*9);
            returnSize[i] = 8;
            strcpy(result[i], multiply15);
        } else if (j%5==0) {
            result[i] = (char*)malloc(sizeof(char)*5);
            returnSize[i] = 4;
            strcpy(result[i], multiply5);
        } else if (j%3==0) {
            result[i] = (char*)malloc(sizeof(char)*5);
            returnSize[i] = 4;
            strcpy(result[i], multiply3);
        } else {
            l = 0;
            while (j>0) {
                j /= 10;
                l++;
            }
            result[i] = (char*)malloc(sizeof(char)*(l+1));
            returnSize[i] = l;
            j = i+1;m=0;
            l--;
            while (j>0) {
                k = j % 10;
                j /= 10;
                result[i][l-m] = '1'+(k-1);
                m++;
            }
            result[i][m] = '\0';
        }
    }
    return result;
}


int main() {
    int n,i;
    int* returnSize;
    char** result;
    // printf("Please input n:");
    // scanf("%d", &n);
    n = 100;
    returnSize = (int*)malloc(sizeof(int)*n);
    printf("fizzBuzzing...\n");
    result = fizzBuzzBad(n, returnSize);
    for (i=0;i<n;i++) {
        printf("%d\t%s\tlen:%d\n", i+1, result[i], returnSize[i]);
    }
}
