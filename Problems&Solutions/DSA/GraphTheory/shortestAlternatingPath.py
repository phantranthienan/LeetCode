# 1129. Shortest Path with Alternating Colors
# You are given an integer n, the number of nodes in a directed 
# graph where the nodes are labeled from 0 to n - 1. Each edge is 
# red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

# redEdges[i] = [ai, bi] indicates that there is a directed red edge 
# from node ai to node bi in the graph, and blueEdges[j] = [uj, vj] indicates 
# that there is a directed blue edge from node uj to node vj in the graph.

# Return an array answer of length n, where each answer[x] is the length of 
# the shortest path from node 0 to node x such that the edge colors alternate 
# along the path, or -1 if such a path does not exist
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

