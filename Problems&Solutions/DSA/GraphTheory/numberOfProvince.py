# 547. Number of Provinces

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

