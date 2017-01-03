int rangeBitwiseAnd(int m, int n) {
    while (n > m) {
        n &= (n-1);
    }
    return m&n;
    
    // 原方法
    // if m<2^i<=n, return 0
    // else 2^(i-1)<m<=n<2^i return self(m-2^(i-1), n-2^(i-1))
    if (m==0)
        return 0;
    unsigned long num=1;
    while(num<=m) {
        num <<= 1;
    }
    if (n>=num)
        return 0;
    num >>= 1;
    return num | rangeBitwiseAnd(m-num, n-num);
}
