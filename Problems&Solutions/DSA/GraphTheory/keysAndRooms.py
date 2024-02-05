# 841. Keys and Rooms
# There are n rooms labeled from 0 to n - 1 and all the rooms are locked 
# except for room 0. Your goal is to visit all the rooms. However, you 
# cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. Each 
# key has a number on it, denoting which room it unlocks, and you can take 
# all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain 
# if you visited room i, return true if you can visit all the rooms, or false otherwise.
def canVisitAllRooms(rooms):
    n = len(rooms)
    canEnter = [False] * n
    canEnter[0] = True
    queue = []
    queue.append(0)

    while queue:
        current = queue.pop(0)
        for next in rooms[current]:
            if not canEnter[next]:
                canEnter[next] = True
                queue.append(next)
                
    nbRoomCanEnter = 0
    for i in range(n):
        if canEnter[i]:
            nbRoomCanEnter += 1
    
    return nbRoomCanEnter == n

