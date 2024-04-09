# 2104. Sum of Subarray Ranges
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
    