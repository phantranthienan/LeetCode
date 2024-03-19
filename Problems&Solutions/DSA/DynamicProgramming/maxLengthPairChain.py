# 646. Maximum Length of Pair Chain
# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

# Return the length longest chain which can be formed.

# You do not need to use up all the given intervals. You can select pairs in any order.

#greedy approach
def greedyLongestChain(pairs):
    pairs.sort(key = lambda x: x[1])
    count = 1
    finish = pairs[0][1]
    for i in range(1, len(pairs)):
        if pairs[i][0] > finish:
            count += 1
            finish = pairs[i][1]

    return count