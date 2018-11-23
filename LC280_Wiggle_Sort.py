"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
"""


def wiggleSort(self, nums):
  """
  :type nums: List[int]
  :rtype: void Do not return anything, modify nums in-place instead.
  """
  
  # for i in range(len(nums)):
  #   nums[i:i+2] = sorted(nums[i:i+2], reverse=i%2)

  swap = True
  for i in range(1, len(nums)):
    if swap:
      if nums[i-1] > nums[i]:
        nums[i-1], nums[i] = nums[i], nums[i-1]
    else:
      if nums[i-1] < nums[i]:
        nums[i-1], nums[i] = nums[i], nums[i-1]
    swap = not swap