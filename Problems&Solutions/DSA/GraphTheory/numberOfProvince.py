# 547. Number of Provinces
# There are n cities. Some of them are connected, while some are not. 
# If city a is connected directly with city b, and city b is connected 
# directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 
# if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

def findCircleNum(isConnected):
    visited = set()
    res = 0
    for i in range(len(isConnected)):
        if i not in visited:
            toVisit = [i]
            while len(toVisit):
                current = toVisit.pop()
                if current not in visited:
                    visited.add(current)
                    toVisit += [j for j, v in enumerate(isConnected[current]) if v and j not in visited]
            res += 1
    return res

