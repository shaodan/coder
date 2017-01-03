#include <stdio.h>
#include <stdlib.h>
#include <time.h>


char* licenseKeyFormatting(char* S, int K) {
    int i=0, j=0, len=0, first, dash_num;
    char *res;
    while (S[i] != '\0') {
        if (S[i] != '-') {
            // a:97 A:65 z:122 Z:90
            S[j++] = S[i]>=97 ? S[i]-32 : S[i];
        }
        i++;
    }
    len = j;
    dash_num = (len-1) / K;
    first = len % K;
    if (first == 0)
        first = K;
    K++;
    len += dash_num+1;
    res = (char *)malloc(sizeof(char)*(len));
    // res[0] = S[0];
    for (i=0,j=0;i<len-1;i++) {
        res[i] = i%K==first ? '-' : S[j++];
    }
    res[i] = '\0';
    return res;
}

// todo : case with serial dash
char* licenseKeyFormatting2(char* S, int K) {
    int i=0, j=0, len=0, first, dash_num, k;
    char *res;
    while (S[i] != '\0') {
        len += S[i] == '-' ? 0 : 1;
        i++;
    }
    // printf("%d\n", len);
    dash_num = (len-1) / K;
    first = len % K;
    if (first == 0 && len > 0)
        first = K;
    len += dash_num+1;
    res = (char *)malloc(sizeof(char)*(len));

    for (i=0, j=0;i<first;i++) {
        j += S[j]=='-' ? 1:0;
        res[i] = S[j] >= 97 ? S[j]-32 : S[j];
        j ++;
    }
    for (;i<len-1;) {
        res[i++] = '-';
        for (k=0;k<K;k++) {
            j += S[j]=='-'? 1:0;
            res[i++] = S[j] >= 97 ? S[j]-32 : S[j];
            j ++;
        }
    }
    res[i] = '\0';
    return res;
}

int main() {
    char input1[] = "2-4A0r7-4-0k2o1";
    char input2[] = "2-4A0r7-4-0k2o1";
    // char input2[] = "--a-a-a-a--";
    int K1 = 2, i;
    clock_t start, finish;
    start = clock();
    printf("%s\n", licenseKeyFormatting(input1, K1));
    for (i=0;i<1000;i++) {
        licenseKeyFormatting(input1, K1);
    }
    finish = clock();
    printf("%f seconds\n",(double)(finish-start));


    start = clock();
    printf("%s\n", licenseKeyFormatting2(input2, K1));
    for (i=0;i<1000;i++) {
        licenseKeyFormatting2(input2, K1);
    }
    finish = clock();
    printf("%f seconds\n",(double)(finish-start));
    return 0;
}
