# 740. Delete and Earn
def deleteAndEarn(nums):
    points = [0] * (max(nums) + 1)
    for num in nums:
        points[num] += num
    
    prev, curr = 0, 0
    for point in points:
        prev,  curr = curr, max(prev + point, curr)
    return curr