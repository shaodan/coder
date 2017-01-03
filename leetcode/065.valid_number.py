class Solution:
    # @param {string} s
    # @return {boolean}
	def isNumber(self,s):
		START = 0
		FAIL = 199
		# 0 start state, waiting for char other than <space>
		# 1 input only num
		# 2 input num  .
		# 3 input num  e or num.num e
		# 4 input ends with <space>
		# 5 input num . num
		# 6 input num e num
		# 7 input only .
		# 8 input only +/-
		# 9 input num e +/-
		# FAIL failure, return false
		state = START
		for c in s:
			if state == FAIL:
				return False
			if state == 0:
				if c=='-' or c=='+':
					state = 8
				elif c>='0' and c<='9':
					state = 1
				elif c == '.':
					state = 7
				elif c==' ':
					continue
				else:
					state = FAIL
			elif state == 1:
				if c>='0' and c<='9':
					continue
				elif c == '.':
					state = 2
				elif c=='e':
					state = 3
				elif c==' ':
					state = 4
				else:
					state = FAIL
			elif state == 2:
				if c>='0' and c<='9':
					state = 5
				elif c=='e':
					state = 3
				elif c==' ':
					state = 4
				else:
					state = FAIL
			elif state == 3:
				if c=='-' or c=='+':
					state = 9
				elif c>='0' and c<='9':
					state = 6
				else:
					state = FAIL
			elif state == 4:
				if c==' ':
					continue
				else:
					state = FAIL
			elif state == 5:
				if c>='0' and c<='9':
					state = 5
				elif c=='e':
					state = 3
				elif c==' ':
					state = 4
				else:
					state = FAIL
			elif state == 6:
				if c>='0' and c<='9':
					state = 6
				elif c==' ':
					state = 4
				else:
					state = FAIL
			elif state == 7:
				if c>='0' and c<='9':
					state = 5
				else:
					state = FAIL
			elif state == 8:
				if c>='0' and c<='9':
					state = 1
				elif c == '.':
					state = 7
				else:
					state = FAIL
			else :
				if c>='0' and c<='9':
					state = 6
				else:
					state = FAIL
		if state == 1 or state == 2 or state == 4 or state == 5 or state == 6 :
			return True
		return False

s = Solution()
ss = ["0", " 0.1 ", "abc", "1 a", "2e10"]
for x in ss:
    print '"%s" => %r' % (x, s.isNumber(x))
