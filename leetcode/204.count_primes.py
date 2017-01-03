def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 3:
        return 0
    if n < 5:
        return n-2
    count = 0
    is_prime = [True]*(n)
    is_prime[0] = False
    is_prime[1] = False
    last_prime = 2
    while last_prime < n-1:
        for i in xrange(last_prime+1, n):
            if is_prime[i]:
                count += 1
                last_prime = i
                for j in xrange(2, (n-1)/i):
                    is_prime[i*j] = False
                break
        if i==n:
            break
    return count

print countPrimes(100)
