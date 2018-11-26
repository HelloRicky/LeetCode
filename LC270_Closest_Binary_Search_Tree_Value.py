"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        result_node = root.val
        min_gap = float('inf')
        node = root
        while node != None:
          tmp_gap = abs(node.val - target)
          if tmp_gap < min_gap:
            min_gap = tmp_gap
            result_node = node.val
          if node.val >= target:
            node = node.left
          else:
            node = node.right
        return result_node