# Given a binary tree where node values are digits from 1 to 9. 
# A path in the binary tree is said to be pseudo-palindromic 
# if at least one permutation of the node values in the path is a palindrome.

# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countOdd(self, list):
        count = 0
        for i in list:
            if i % 2 != 0:
                count += 1 
        return count 

    def pseudoPalindromicPaths (self, root):    
        frequency = [0] * 10
        return self.dfs(root, frequency)
    
    def dfs(self, root, frequency):
        if not root:
            return 0
        
        frequency[root.val] += 1
        if not root.left and not root.right:
            Odd = self.countOdd(frequency)
            frequency[root.val] -= 1
            return 1 if Odd <= 1 else 0
        
        leftCount = self.dfs(root.left, frequency)
        rightCount = self.dfs(root.right, frequency)
        
        frequency[root.val] -=  1
        return leftCount + rightCount