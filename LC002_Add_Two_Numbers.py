"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
       ## my solution 
#         return self._addTwoNumbers(l1, l2)
        
#     def _addTwoNumbers(self, l1, l2, carrier=0):
#       if not l1 and not l2: return self._process(l1, carrier)
#       if not l1: return self._process(l2, carrier)
#       if not l2: return self._process(l1, carrier)

#       _sum = l1.val+ l2.val+ carrier
#       carrier = _sum //10
#       result = _sum %10
#       l1.val = result
#       l1.next = self._addTwoNumbers(l1.next, l2.next, carrier)
#       return l1
    
#     def _process(self, l1, carrier=0):
#       if not carrier: return l1
#       if not l1: return ListNode(carrier)
#       _sum = l1.val + carrier
#       carrier = _sum//10
#       result = _sum % 10
#       l1.val = result
#       l1.next = self._process(l1.next, carrier)
#       return l1


      ## top java solution but slow
        dummyHead = ListNode(0)
        p = l1
        q = l2
        curr = dummyHead
        carry = 0
        while p or q:
          x = p.val if p else 0
          y = q.val if q else 0
          _sum = carry + x + y
          carry = _sum // 10
          curr.next = ListNode(_sum % 10)
          curr = curr.next
          if p: p = p.next
          if q: q = q.next
        if carry:
          curr.next = ListNode(carry)
        return dummyHead.next