class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if len(bank) ==0:
            return -1
        bank = set(bank)
        if end not in bank:
            return -1

        import Queue
        q = Queue.Queue()
        q.put((start, 0))

        def mutate(gene):
            for i in xrange(8):
                for c in ['A', 'C', 'G', 'T']:
                    if c == gene[i]:
                        continue
                    yield gene[:i]+c+gene[i+1:]

        while not q.empty():
            gene, step = q.get()
            for mutation in mutate(gene):
                if mutation == end:
                    return step+1
                if mutation in bank:
                    q.put((mutation, step+1))
                    bank.remove(mutation)
        return -1



s = Solution()
# start = "AAAAACCC"
# end = "AACCCCCC"
# bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# start= "AACCGGTT"
# end=   "AAACTGTA"
# bank= ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
start = "AACCGGTT"
end =   "AACCGGTA"
bank = []
print s.minMutation(start, end, bank)
