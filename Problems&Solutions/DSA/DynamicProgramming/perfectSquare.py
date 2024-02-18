# 279. Perfect Squares
# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, 
# it is the product of some integer with itself. For example, 1, 4, 9, and 16 are 
# perfect squares while 3 and 11 are not.

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
