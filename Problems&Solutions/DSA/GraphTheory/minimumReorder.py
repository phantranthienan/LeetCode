# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# There are n cities numbered from 0 to n - 1 and n - 1 roads such that 
# there is only one way to travel between two different cities (this network form a tree). 
# Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] 
# represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city 
# can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

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
        
    
     
