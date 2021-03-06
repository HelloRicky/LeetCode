"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
        #            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        # if len(digits) == 0:
        #     return []
        # if len(digits) == 1:
        #     return list(mapping[digits[0]])
        # prev = self.letterCombinations(digits[:-1])
        # additional = mapping[digits[-1]]
        # return [s + c for s in prev for c in additional]
        
        map_ = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        result = []
        
        def make_combinations(i, cur):
            if i == len(digits):
                if len(cur) > 0:
                    result.append(''.join(cur))
                return
            for ch in map_[digits[i]]:
                cur.append(ch)
                make_combinations(i+1, cur)
                cur.pop()
        
        make_combinations(0, [])
        
        return result

          