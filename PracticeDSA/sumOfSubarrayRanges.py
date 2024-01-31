# You are given an integer array nums. 
# The range of a subarray of nums is the 
# difference between the largest and smallest element in the subarray.

# Return the sum of all subarray ranges of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.

def subArrayRanges(nums):
    tableMax = [[0] * len(nums) for _ in range(len(nums))]
    tableMin = [[0] * len(nums) for _ in range(len(nums))]
    for i in range(len(nums)):
        tableMax[i][i] = nums[i]
        tableMin[i][i] = nums[i]

    sums = []
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            tableMax[i][j] = max(tableMax[i][j-1], nums[j])
            tableMin[i][j] = min(tableMin[i][j-1], nums[j])
            sums.append(tableMax[i][j] - tableMin[i][j])

    return sum(sums)
    
def subArrayRanges2(nums):
    res = 0
    for i in range(len(nums)):
        maxVal = nums[i]
        minVal = nums[i]
        for j in range(i+1, len(nums)):
            max = max(maxVal, nums[j])
            min = min(minVal, nums[j])
            res += maxVal - minVal
    return res

    