# 1376. Time Needed to Inform All Employees

def numOfMinutes(n, headID, manager, informTime):
    employees = [[] for _ in range(n)]
    for i in range(n):
        if manager[i] >= 0:
            employees[manager[i]].append(i)

    print(employees)

    def dfs(i):
        return max([dfs(j) for j in employees[i]] + [0]) + informTime[i]
    
    return dfs(headID)

n,headID = 6, 2 
manager, informTime = [2,2,-1,2,2,2], [0,0,1,0,0,0]
numOfMinutes(n, headID, manager, informTime)
