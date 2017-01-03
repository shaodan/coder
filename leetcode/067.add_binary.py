class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l_a = len(a)
        l_b = len(b)

        m = [('0', 0), ('1', 0), ('0', 1), ('1', 1)]
        if l_a < l_b:
            l_a, l_b = l_b, l_a
            a, b = b, a
        l_l = l_a - l_b
        a_left = a[:l_l]
        a = a[l_l:]
        carry = 0
        res_right = ['0']*l_b
        for i in xrange(l_b-1, -1, -1):
            add = ord(a[i]) + ord(b[i]) + carry - 96
            res_right[i], carry = m[add]

        if carry == 0:
            res_left = a_left
        else:
            for i in xrange(l_l-1, -1, -1):
                if a_left[i]=='0':
                    break
            if i==0:
                res_left = '1' + '0' * l_l
            else:
                res_left = a_left[:i] + '1' + '0' * (l_l-i-1)
        return res_left + ''.join(res_right)

a="10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
b="110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"
a = '111'
b = '1'
s = Solution()
print s.addBinary(a,b)
