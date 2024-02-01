# 2104. Sum of Subarray Ranges
# You are given an integer array nums. 
# The range of a subarray of nums is the 
# difference between the largest and smallest element in the subarray.

# Return the sum of all subarray ranges of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.

def subArrayRanges(nums):
    res = 0
    for i in range(len(nums)):
        maxVal = nums[i]
        minVal = nums[i]
        for j in range(i+1, len(nums)):
            maxVal = max(maxVal, nums[j])
            minVal = min(minVal, nums[j])
            res += maxVal - minVal
    return res
    
def subArrayRanges2(A0):
    res = 0
    inf = float('inf')
    A = [-inf] + A0 + [-inf]
    s = []
    for i in range(len(A)):
        while s and A[s[-1]] > A[i]:
            j = s.pop()
            k = s[-1]
            res -= A[j] * (i - j) * (j - k)
        s.append(i)
        
    A = [inf] + A0 + [inf]
    s = []
    for i in range(len(A)):
        while s and A[s[-1]] < A[i]:
            j = s.pop()
            k = s[-1]
            res += A[j] * (i - j) * (j - k)
        s.append(i)
    return res
    