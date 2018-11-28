"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        ## while loop
        # prev = None
        # while head:
        #   cur = head
        #   head = head.next
        #   cur.next = prev
        #   prev = cur
        # return prev
        
        return self._reverseList(head)
        
        ## recursive
    def _reverseList(self, head, prev = None):
      if not head:
        return prev
      node =head.next
      head.next = prev
      return self._reverseList(node, head)