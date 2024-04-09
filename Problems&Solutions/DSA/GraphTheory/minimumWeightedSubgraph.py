# 2203. Minimum Weighted Subgraph With the Required Paths
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