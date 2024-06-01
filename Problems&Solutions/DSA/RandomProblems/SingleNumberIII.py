# 260. Single Number III

def singleNumber(nums):
    from collections import defaultdict
    count = defaultdict(int)
    for num in nums:
        count[num] += 1

    ans = []
    for num in count:
        if count[num] == 1:
            ans.append(num)

    return ans

print (singleNumber([1,2,1,3,2,5]))