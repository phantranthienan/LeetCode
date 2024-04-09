# 221. Maximal Square
def maximalSquare(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            matrix[i][j] = int(matrix[i][j])

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                matrix[i][j] = matrix[i][j] + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])

    max_side = max([max(matrix[i]) for i in range(m)])
    return max_side * max_side