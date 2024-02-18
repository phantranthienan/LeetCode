# 72. Edit Distance
# Given two strings word1 and word2, return the minimum number of operations 
# required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

# !Levenshtein distance

#recursive approach
def recursiveMinDistance(word1, word2):
    if not word1 and not word2:
        return 0
    
    if not word1:
        return len(word2)
    
    if not word2:
        return len(word1)
    
    if word1[0] == word2[0]:
        return recursiveMinDistance(word1[1:], word2[1:])
    
    insert = 1 + recursiveMinDistance(word1, word2[1:])
    delete = 1 + recursiveMinDistance(word1[1:], word2)
    replace = 1 + recursiveMinDistance(word1[1:], word2[1:])

    return min(insert, delete, replace)

#dynamic approach
def dynamicMinDistance(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    matrixDp = [[0]*(len1 + 1) for _ in range(len2 + 1)]

    for i in range(len1 + 1):
        matrixDp[i][0] = i

    for j in range(len2 + 1):
        matrixDp[0][j] = j
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if word1[i - 1] == word2[j - 1]:
                matrixDp[i][j] = matrixDp[i - 1][j - 1]
            else: 
                matrixDp[i][j] = 1 + min(
                    matrixDp[i - 1][j],
                    matrixDp[i][j - 1],
                    matrixDp[i - 1][j - 1]
                )
    
    return matrixDp[-1][-1]