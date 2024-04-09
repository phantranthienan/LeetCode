# 802. Find Eventual Safe States
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


