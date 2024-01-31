# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
# return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to 
# its traversing-order next in the array, which means you could search circularly 
# to find its next greater number. If it doesn't exist, return -1 for this number.

def nextGreaterElements(self, nums):
    n = 2 * len(nums)
    res = [-1] * len(nums)
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i % len(nums)]:
            res[stack.pop()] = nums[i % len(nums)]
        stack.append(i % len(nums))