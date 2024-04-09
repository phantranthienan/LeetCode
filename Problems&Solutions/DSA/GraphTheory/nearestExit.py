# 1926. Nearest Exit from Entrance in Mazes
def nearestExit(maze, entrance):
    direction_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    queue = []
    visited = []
    m, n = len(maze), len(maze[0])
    for i in range(4):
        queue.append([entrance[0] + direction_list[i][0], entrance[1] + direction_list[i][1]])
    count = 0
    while queue:
        cell = queue.pop(0)
        if (cell[0] == 0 or cell[1] == 0 or cell[0] == m - 1 or cell[1] == n - 1):
            return count
        if cell not in visited:
            visited.append(cell)


