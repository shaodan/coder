#include <stdio.h>
typedef enum { false, true } bool;


void reverseWord(char *s, int i, int j) {
    char t;
    for (;i<j;i++,j--) {
        t = s[i];
        s[i] = s[j];
        s[j] = t;
    }
}

int stripWords(char *s) {
    int i=1,j=0;
    if (s[0] != ' ') {
        while(s[i]!='\0') {
            if (s[i] != ' '|| s[i-1]!=' ')
                i++;
            else {
                i++;
                break;
            }
        }
        j = i;
    }
    while(s[i]!='\0') {
        if (s[i] != ' ' || s[i-1]!=' ') {
            s[j++] = s[i];
        }
        i++;
    }
    if (j>0 && s[j-1]==' ')
        j--;
    s[j] = '\0';
    // if has no space at all 
    //     return -j;
    return j;
}

void reverseWords(char *s) {
    int len,i,j;
    len = stripWords(s);
    if (len==0)
        return;
    reverseWord(s, 0, len-1);

    for (i=0;i<len;) {
        for (j=i;j<len&&s[j]!=' ';j++) {}
        reverseWord(s, i, j-1);
        i = j+1;
    }
}


int main() {
	char s1[] = "the sky is blue";
	char s2[] = " the   sky is blue! ";
	char s3[] = "they";
	char s4[] = "  ";
    char* ss[4] = {s1, s2, s3, s4};
    char* s;
    int i;
    for (i=0;i<4;i++){
        s = ss[i];
        printf("'%s' ==> ", s);
        reverseWords(s);
        printf("'%s'\n", s);
    }
    return 0;
}
