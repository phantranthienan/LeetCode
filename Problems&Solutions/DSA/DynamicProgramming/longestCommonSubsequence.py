# 1143. Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some 
# characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

def recursiveLCS(text1, text2):
    if not text1 or not text2:
        return 0
    
    if text1[0] == text2[0]:
        return 1 + longestCommonSubsequence(text1[1:], text2[1:])
    else:
        return max(
            longestCommonSubsequence(text1[1:], text2),
            longestCommonSubsequence(text1, text2[1:])
        )
        

def longestCommonSubsequence(text1, text2):
    m = len(text1)
    n = len(text2)

    dp = [[0]*(n + 1) for _ in range(m + 1)]

    for i in range(1, m):
        for j in range(1, n):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]
    