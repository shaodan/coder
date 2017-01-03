class Solution {

    public static void main(String[] args) {
        String s = "abcdefg";
        int k = 2;
        Solution sol = new Solution();
        String s2 = sol.reverseStr(s, k);
        System.out.println(s);
        System.out.println(s2);
    }

    public String reverseStr(String s, int k) {
        if (k==1) 
            return s;
        char[] c = s.toCharArray();
        int l = s.length();
        int i=0;
        while (i < l) {
            reverse(c, i, min(l-1, i+k-1));
            i += 2*k;
        }
        return String.valueOf(c);
    }
    public void reverse(char[] c, int l, int r) {
        char t;
        while (l < r) {
             t = c[l];
             c[l++] = c[r];
             c[r--] = t;
        }
    }
    public int min(int a, int b) {
        return a > b ? b : a;
    }
}
