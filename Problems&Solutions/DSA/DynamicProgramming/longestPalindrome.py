# 5. Longest Palindromic Substring
# Given a string s, return the longest 
# palindromic substring in s.
def longestPalindrome(s):
    n = len(s)
    dp = [[1]*n for _ in range(n)]
    res_i, res_j = 0, 0
    for sub_length in range(2, n + 1):
        for i in range(n - sub_length + 1):
            j = i + sub_length - 1
            if s[i] == s[j]:                        
                if sub_length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i+1][j-1] + 2 if dp[i+1][j-1] else 0
                    
                if dp[i][j] >= res_j - res_i + 1:
                    res_i, res_j = i, j
            else:
                dp[i][j] = 0
    return s[res_i: res_j + 1]