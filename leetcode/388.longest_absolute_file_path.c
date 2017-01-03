#include <stdio.h>
#include <stdbool.h>

int lengthLongestPath(char* input) {
    int i=0,j,d,max_l=0;
    int l[1000];
    bool isFile;
    if (input == NULL)
        return 0;
    l[0] = 0;
    while (input[i]!='\0') {
        d = 0;
        isFile=false;
        while (input[i]=='\t') {
            d++;
            i++;
        }
        j = l[d];
        while (input[i]!='\0' && input[i]!='\n') {
            if (!isFile && input[i]=='.') {
                isFile = true;
            }
            i++;
            j++;
        }
        if (isFile) {
            if (j > max_l)
                max_l = j;
        } else {
            l[d+1] = j+1;
        }
        if (input[i]!='\0')
            i++;
    }
    return max_l;
}

int main() {
    char input1[] = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext";
    char input2[] = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext";
    printf("longest path in input1:%d(should be 20)\n", lengthLongestPath(input1));
    printf("longest path in input2:%d(should be 32)\n", lengthLongestPath(input2));
}
