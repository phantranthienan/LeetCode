# 1944. Number of Visible People in a Queue

def canSeePersonsCount(heights):
    res = [0] * len(heights)
    stack = []
    for i in range(len(heights)):
        while stack and heights[i] > heights[stack[-1]]:
            res[stack.pop()] += 1
        if stack:
            res[stack[-1]] += 1
        stack.append(i)
    return res