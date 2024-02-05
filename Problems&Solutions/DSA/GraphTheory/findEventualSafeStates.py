# 802. Find Eventual Safe States
# There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
# The graph is represented by a 0-indexed 2D integer array graph where graph[i] 
# is an integer array of nodes adjacent to node i, meaning there is an edge from 
# node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges. A node is a safe node 
# if every possible path starting from that node leads to a terminal node (or another safe node).

# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

# Approach 1: Topological Sort Using Kahn's Algorithm
def eventualSafeNodes(self, graph):
        n = len(graph)
        out_degree = [0 for _ in range(n)]
        safe = [False for _ in range(n)]
        R = [[] for _ in range(n)]
        q = []
        ans = []

        for i in range(n):
            for j in graph[i]:
                R[j].append(i)
            out_degree[i] = len(graph[i])
            if out_degree[i] == 0:
                q.append(i)
        
        while q:
            u = q.pop(0)
            safe[u] = True
            for v in R[u]:
                out_degree[v] -= 1
                if (out_degree[v] == 0):
                    q.append(v)
        
        for i in range(n):
            if safe[i]:
                ans.append(i)
        
        return ans

# Approach 2: DFS


