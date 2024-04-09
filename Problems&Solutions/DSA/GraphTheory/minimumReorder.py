# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# DFS Approach
def minReorder(n, connections):
    neighbors = [[] for _ in range(n)]
    for [i, j] in connections:
        neighbors[i].append(j)
        neighbors[j].append(-i)
    visited = [False]*n
    def dfs(city, visited):
        count = 0
        visited[city] = True
        for neighbor in neighbors[city]:
            if not visited[abs(neighbor)]:
                count += dfs(abs(neighbor), visited) + (1 if neighbor > 0 else 0)
        return count
    return dfs(0, visited)

#BFS Approach
def minReorderBFS(n, connections):
    neighbors = [[] for _ in range(n)]
    for [i, j] in connections:
        neighbors[i].append([j, 1])
        neighbors[j].append([i, 0])
    queue = [0]
    visited = [False]*n
    count = 0
    while queue:
        city = queue.pop(0)
        visited[city] = True
        for neighbor, flag in neighbors[city]:
            if not visited[neighbor]:
                count += flag
                queue.append(neighbor)
    return count
        
    
     
