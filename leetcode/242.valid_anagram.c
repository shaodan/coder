bool isAnagram(char* s, char* t) {
    int i;
    int count[26];
    memset(count, 0, sizeof(int)*26);
    for (i=0;;i++) {
        if (s[i]=='\0') {
            if (t[i]!='\0')
                return false;
            break;
        }
        count[s[i]-'a']++;
        count[t[i]-'a']--;
    }
    for (i=0;i<26;i++) {
        if (count[i]!=0)
            return false;
    }
    return true;
}
