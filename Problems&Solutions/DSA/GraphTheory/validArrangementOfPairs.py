
# 2097. Valid Arrangement of Pairs
# You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. 
# An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, 
# we have endi-1 == starti.

# Return any valid arrangement of pairs.

# Note: The inputs will be generated such that there exists a valid arrangement of pairs.

from collections import defaultdict

def validArrangement(pairs):
    graph = defaultdict(list)
    degree = defaultdict(int)
    for x, y in pairs:
        graph[x].append(y)
        degree[x] += 1
        degree[y] -= 1
    for k in degree:
        if degree[k] == 1:
            x = k
            break
    ans = []
    stack = [x]
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        ans.append(stack.pop())
    ans.reverse()
    
    return [[ans[i], ans[i + 1]] for i in range(len(ans)-1)]

def validArrangement2(pairs):
    graph = defaultdict(list)
    degree = defaultdict(int) 
    for x, y in pairs: 
        graph[x].append(y)
        degree[x] += 1
        degree[y] -= 1
            
    for k in degree: 
        if degree[k] == 1: 
            x = k
            break 
            
    ans = []
    def findEulerPath(x): 
        while graph[x]: findEulerPath(graph[x].pop()) 
        ans.append(x)
    findEulerPath(x)
    ans.reverse()
    return [[ans[i], ans[i+1]] for i in range(len(ans)-1)]