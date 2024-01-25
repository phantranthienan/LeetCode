# Given an array arr of positive integers, consider all binary trees such that:

# Each node has either 0 or 2 children;
# The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
# The value of each non-leaf node is equal to the product of the largest leaf value 
# in its left and right subtree, respectively.

# Among all possible binary trees considered, 
# return the smallest possible sum of the values of each non-leaf node. 
# It is guaranteed this sum fits into a 32-bit integer.

# A node is a leaf if and only if it has zero children.
def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print("{:4}".format(val), end=' ')
        print()

#DP solution, bottom-up apppoach 
class BottomUpSolution(object):
    def mctFromLeafValues(self, arr):
        dp = [[0]*len(arr) for i in range(len(arr))]
        
        for subLength in range (1, len(arr) + 1):
            for i in range(len(arr) - subLength + 1):
                j = i + subLength - 1
                if (subLength == 1):
                    dp[i][j] = arr[i]
                elif (subLength == 2):
                    dp[i][j] = arr[i] * arr[j]
                else:
                    res = 2**31
                    for k in range(i, j):
                        nodeValue = max(arr[i:k+1]) * max(arr[k+1:j+1])
                        leftValue = dp[i][k] if k - i >= 1 else 0
                        rightValue = dp[k+1][j] if j - k - 1 >= 1 else 0
                        res = min(res, nodeValue + leftValue + rightValue)
                    dp[i][j] = res
        return dp[0][len(arr) - 1] 
         


Solution().mctFromLeafValues([6,2,4])


