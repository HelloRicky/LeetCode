"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1

"""


class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        ## my solution
#         wl1 = []
#         wl2 = [] 
#         for i, word in enumerate(words):
#           if word == word1: wl1.append(i)
#           if word == word2: wl2.append(i)
#           continue
          
#         min_result = len(words)
#         for i in wl1:
#           for j in wl2:
#             tmp_min = abs(i-j)
#             if tmp_min< min_result:
#               min_result = tmp_min
#         return min_result
        
        ## top solution
        a = b = min_result = len(words)

        for i, word in enumerate(words):
          if word == word1:
            a = i
          elif word == word2:
            b = i
          else:
            continue
          
          tmp_min = abs(a-b)
          if tmp_min< min_result:
            min_result = tmp_min
        return min_result
          