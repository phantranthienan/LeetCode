# 1306. Jump Game III

def canReach(arr, start):
    queue = [start]
    visited = [False]*len(arr)
    while queue:
        jump_index = queue.pop(0)
        right_dest = jump_index + arr[jump_index] if jump_index + arr[jump_index] < len(arr) else None
        left_dest = jump_index - arr[jump_index] if jump_index - arr[jump_index] >= 0 else None
        if right_dest is not None and not visited[right_dest]:
            if arr[right_dest] == 0:
                return True
            else:
                visited[right_dest] = True
                queue.append(right_dest)
        
        if left_dest is not None and not visited[left_dest]:
            if arr[left_dest] == 0:
                return True
            else:
                visited[left_dest] = True
                queue.append(left_dest)
    
    return False

arr = [0,1]
start = 1
print(canReach(arr, start))