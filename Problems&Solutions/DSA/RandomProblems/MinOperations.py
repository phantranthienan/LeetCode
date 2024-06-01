# 2870. Minimum Number of Operations to Make Array Empty
def minOperations(nums):
    from collections import defaultdict
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    ans = 0
    for num in count:
        if count[num] == 1:
            return -1
        ans += count[num]/3 
        if (count[num]%3 != 0):
            ans += 1
    return ans