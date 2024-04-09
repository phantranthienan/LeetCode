# 841. Keys and Rooms
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

