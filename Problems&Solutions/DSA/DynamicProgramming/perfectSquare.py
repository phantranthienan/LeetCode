# 279. Perfect Squares
#dynamic approach
def numSquares(self, n):
    dp = [float('inf')]*(n+1)
    dp[0] = 0
    count = 1
    while count**2 <= n:
        for i in range(count**2, n + 1):
            dp[i] = min(dp[i - count**2] + 1, dp[i])
        count += 1
    return dp[n]

# mathematical approach
# Lagrange's four-square theorem, also known as Bachet's conjecture, 
# states that every natural number can be represented as a sum of 
# four non-negative integer squares.[1] That is, the squares form an additive basis of order four.
