# 646. Maximum Length of Pair Chain
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