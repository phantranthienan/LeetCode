from math import factorial
# 62. Unique Paths
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