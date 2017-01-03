class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 3:
            return s
        ord_A = ord(' ')
        count = [0]*(ord('z') - ord_A+1)
        for c in s:
            count[ord(c)-ord_A] += 1
        count_f = filter(lambda t: t[1]>0, enumerate(count))
        res = sorted(count_f, key=lambda t: t[1], reverse = True)
        return ''.join([chr(t[0]+ord_A)*t[1] for t in res])
        
