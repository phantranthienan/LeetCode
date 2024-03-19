# 200. Number of Islands
# Given an m x n 2D binary grid grid which represents a map of 
# '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting 
# adjacent lands horizontally or vertically. You may assume all 
# four edges of the grid are all surrounded by water.
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

def numIslands(grid):
    m = len(grid)
    n = len(grid[0])
    visited = [[False]*n for _ in range(m)]
    queue = []
    nbIslands = 0

    for i in range(m):
        for j in range(n):
            if not visited[i][j] and grid[i][j] == "1":
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    start_i, start_j = queue.pop(0)
                    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        new_i, new_j = start_i + di, start_j + dj
                        if (0 <= new_i < m and 0 <= new_j < n) and grid[new_i][new_j] == "1" and not visited[new_i][new_j]:
                            visited[new_i][new_j] = True
                            queue.append((new_i, new_j))                            
                nbIslands += 1
    return nbIslands

