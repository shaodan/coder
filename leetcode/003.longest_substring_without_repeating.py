class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = [-1] * 127
        max_len = 0
        cur_len = 0
        for i in xrange(len(s)):
            index = ord(s[i])
            dis = i-last[index]
            last[index] = i
            if dis > cur_len:
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len
                cur_len = dis
        if cur_len > max_len:
            max_len = cur_len
        return max_len

if __name__ == '__main__':
    string = "abcabcbb"
    s = Solution()
    l = s.lengthOfLongestSubstring(string)
    print(l)

