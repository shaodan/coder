#
# [126] Word Ladder II
#
# https://leetcode.com/graphql
#
# algorithms
# Hard (14.55%)
# Total Accepted:    76K
# Total Submissions: 521.9K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
# 
# 
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# 
# For example,
# 
# 
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 
# Return
# 
# ⁠ [
# ⁠   ["hit","hot","dot","dog","cog"],
# ⁠   ["hit","hot","lot","log","cog"]
# ⁠ ]
# 
# 
# 
# 
# Note:
# 
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# 
# 
# UPDATE (2017/1/20):
# The wordList parameter had been changed to a list of strings (instead of a
# set of strings). Please reload the code definition to get the latest changes.
# 
#
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        class WordNode(object):
            def __init__(self, prev, rev):
                # self.distance = distance
                self.prev = [prev]
                self.rev = rev

        nodeMap = {}

        wordlist = set(wordlist)
        finished = set()
        found = False


        r = False
        while not found:
            if new_word not in nodeMap:
                nodeMap[new_word] = WordNode(k, nodeMap[word], r)
            else:
                nodeMap[new_word].prev.append(nodeMap[word])
        f

    def findLevel(self, level, r):
        next_level = []
        for word in level:
        return

    def findLadders2(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        # size = len(wordlist)
        # if size == 0:
        #     return []
        # if beginWord == endWord:
        #     return [[beginWord, endWord]]

        # diffs = 0
        # for ch1, ch2 in zip(beginWord, endWord):
        #     if ch1 != ch2:
        #         diffs += 1
        #         if diffs > 1:
        #             break
        # if diffs == 1:
        #     return [[beginWord, endWord]]
        wordlist = set(wordlist)
        # clean begin/end word
        wordlist.discard(beginWord)
        wordlist.discard(endWord)
        # add begin/end word to wordlist's head and tail
        wordlist = list(wordlist)
        word_len = len(beginWord)
        size = len(wordlist)
        if size == 0:
            wordlist.append(beginWord)
        else:
            wordlist.append(wordlist[0])
            wordlist[0] = beginWord
        wordlist.append(endWord)
        size += 2

        # adj matrix of each word
        adj = [None]*size
        for i in xrange(size):
            adj[i] = []
        result = []
        for i in xrange(size):
            word_i = wordlist[i]
            for j in xrange(i+1, size):
                word_j = wordlist[j]
                diffs = 0
                for ch1, ch2 in zip(word_i, word_j):
                    if ch1 != ch2:
                        diffs += 1
                        if diffs > 1:
                            break
                if diffs == 1:
                    adj[i].append(j)
                    adj[j].append(i)
        # print wordlist
        # print adj

        # Dijkstra's algorithm
        distance = [size+1000]*size
        queue = [None]*size     # use list to simulate queue, since weight is 1
        queue_h = 0             # distance of early node in queue is alwasy
        queue_t = 1             # not greater than late one
        prev = [None]*size
        prev[0] = []
        distance[0] = 0
        queue[0] = 0
        finished = set()
        wait = set([0])
        while len(wait)>0:
            i = queue[queue_h]
            # print 'pop head: '+str(i)
            queue_h += 1
            wait.remove(i)
            for j in adj[i]:
                if j not in finished and j not in wait:
                    wait.add(j)
                    queue[queue_t] = j
                    queue_t += 1
                    # print 'add to tail: '+str(j)
                else:
                    dis_j = distance[j] + 1
                    if dis_j < distance[i]:
                        distance[i] = dis_j
                        prev[i] = [j]
                    elif dis_j == distance[i]:
                        prev[i].append(j)
            if i == size-1:
                break
            finished.add(i)
        # print distance
        # print prev

        self.prev = prev
        self.wordlist = wordlist
        pathStr = self.printPath(0, size-1)
        if pathStr is None:
            return []
        for i, path in enumerate(pathStr):
            pathStr[i] = path.split(',')
        return pathStr

    def printPath(self, begin, end):
        if begin == end:
            return [self.wordlist[begin]]
        path = []
        pp = self.prev[end]
        if pp is None:
            return None
        for x in pp:
            pre_path = self.printPath(begin, x)
            if pre_path is None:
                return None
            for p in pre_path:
                path.append(p+','+self.wordlist[end])
        return path

s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
s.findLadders(beginWord, endWord, wordList)
s.printPath(beginWord, endWord)

        
