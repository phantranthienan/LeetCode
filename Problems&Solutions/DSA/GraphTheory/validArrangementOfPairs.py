# 2097. Valid Arrangement of Pairs
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