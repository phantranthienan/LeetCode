# 1129. Shortest Path with Alternating Colors
def shortestAlternatingPaths(n, redEdges, blueEdges):
    G = [[[], []] for _ in range(n)]
    for i, j in redEdges: 
        G[i][0].append(j)
    for i, j in blueEdges:
        G[i][1].append(j)

    res = [0, 0] + [[-1, -1] for _ in range(n - 1)]
    queue = [[0, 0], [0, 1]]
    for i, c in queue:
        for j in G[i][c]:
            if res[j][c] == -1:
                res[j][c] = res[i][1 - c] + 1 #?1 - c always return the opposite of c 
                queue.append([j, 1 - c])
    ans = []
    for i in range(n):
        t = min(res[i][0], res[i][1])
        ans.append(t)
    
    return ans

