from math import factorial
# 62. Unique Paths
# There is a robot on an m x n grid. The robot is initially located at the top-left corner 
# (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot 
# can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

def uniquePaths(m, n):
    return factorial(m+n-2) // factorial(m-1) // factorial(n-1)

# Dynamic programming approach

def uniquePathsDP(m, n):
    dp = [[[1] for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[j][i - 1]
    
    return dp[-1][-1]

def uniquePathDP2(m, n):
    if m < n:
        m, n = n, m
        
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]