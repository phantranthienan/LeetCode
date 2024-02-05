# 740. Delete and Earn
# You are given an integer array nums. You want to maximize the number 
# of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, 
# you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times
def deleteAndEarn(nums):
    points = [0] * (max(nums) + 1)
    for num in nums:
        points[num] += num
    
    prev, curr = 0, 0
    for point in points:
        prev,  curr = curr, max(prev + point, curr)
    return curr