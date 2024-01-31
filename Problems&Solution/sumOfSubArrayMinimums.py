# 907. Sum of Subarray Minimums
# Given an array of integers arr, find the sum of min(b), 
# where b ranges over every (contiguous) subarray of arr. 
# Since the answer may be large, return the answer modulo 109 + 7.

def sumSubarrayMins(arr):
    nextSmaller = [len(arr)] * len(arr)
    prevSmallerOrEqual = [-1] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            nextSmaller[stack.pop()] = i
        stack.append(i)
    
    stack.clear()

    for i in range(len(arr)-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            prevSmallerOrEqual[stack.pop()] = i
        stack.append(i)
    print(nextSmaller)
    print(arr)
    print(prevSmallerOrEqual)
    ans = 0
    for i in range(len(arr)):
        ans += arr[i] * (i - prevSmallerOrEqual[i]) * (nextSmaller[i] - i)
        print(ans)
    return ans % (10**9 + 7)            
arr = [3,1,2,4]

print(sumSubarrayMins(arr))