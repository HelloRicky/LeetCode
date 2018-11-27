"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false

"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        ## my solution
#         d_single = ['0','1','8']
#         d = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
#         l = len(num)
        
#         if l == 1:
#           return True if num in d_single else False
        
#         if l%2:
#           m = num[l/2]
#           if m not in d_single:
#             return False
#         for i in range(l/2):
#           head = num[i]
#           tail = num[-1-i]
#           if (head not in d) or (tail not in d):
#             return False
#           if d[head] != tail:
#             return False
#         return True

        ## top solution
        d = [('0', '0'), ('1','1'),('6','9'),('9','6'),('8','8')]
        i=0
        j=len(num)-1
        while j >= i:
          if (num[i],num[j]) not in d:
            return False
          i +=1
          j -=1
        return True