# 2203. Minimum Weighted Subgraph With the Required Paths
# You are given an integer n denoting the number of nodes of a weighted directed graph. 
# The nodes are numbered from 0 to n - 1.

# You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] 
# denotes that there exists a directed edge from fromi to toi with weight weighti.

# Lastly, you are given three distinct integers src1, src2, and dest denoting three 
# distinct nodes of the graph.

# Return the minimum weight of a subgraph of the graph such that it is possible 
# to reach dest from both src1 and src2 via a set of edges of this subgraph. 
# In case such a subgraph does not exist, return -1.

# A subgraph is a graph whose vertices and edges are subsets of the original graph. 
# The weight of a subgraph is the sum of weights of its constituent edges.
from collections import defaultdict
import heapq

def minimumWeight(self, n, edges, src1, src2, dest):
    def shortestPath(graph, src):
        pq = []
        heapq.heappush(pq, (0, src))
        dist = [float('inf')] * n
        dist[src] = 0

        while pq:
            d, u = heapq.heappop(pq)
            for v, weight in graph[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        return dist

    G1 = defaultdict(list)
    G2 = defaultdict(list)
    for a, b, w in edges:
        G1[a].append((b, w))
        G2[b].append((a, w))
    arr1 = shortestPath(G1, src1)
    arr2 = shortestPath(G1, src2)
    arr3 = shortestPath(G2, dest)
    
    ans = float("inf")
    for i in range(n):
        ans = min(ans, arr1[i] + arr2[i] + arr3[i])
    return ans if ans != float("inf") else -1