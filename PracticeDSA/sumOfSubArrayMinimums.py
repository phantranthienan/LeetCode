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

    ans = 0
    for i in range(len(arr)):
        ans += arr[i] * (i - prevSmallerOrEqual[i]) * (nextSmaller[i] - i)
        print(ans)
    return ans % (10**9 + 7) 

# If A[i-1] <= A[i] then result[i] = result[i-1] + A[i]

# It's easy to see why this happens: our subarrays 
# ending with i-th value are basically same subarrays 
# for (i-1)-th value with extra element A[i] added to 
# each one of them and plus one extra subarray consisting 
# of singular value A[i]. Adding same or bigger value to 
# subarrays doesn't change their minimal values. Thus we 
# can reuse previous sum and account for that extra singular 
# subarray, thus result[i] = result[i-1] + A[i]

# We can generalize
# If we find previous less or equal value A[j] <= A[i] (j<i) 
# then result[i] = result[j] + A[i]*(i-j)           

def sumSubarrayMins2(A):
        A = [0]+A
        result = [0]*len(A)
        stack = [0]
        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                stack.pop() 
            j = stack[-1]
            result[i] = result[j] + (i-j)*A[i]
            stack.append(i)
        return sum(result) % (10**9+7)