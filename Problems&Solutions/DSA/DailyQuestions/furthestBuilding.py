# 1642. Furthest Building You Can Reach
# You are given an integer array heights representing the heights of buildings, 
# some bricks, and some ladders.

# You start your journey from building 0 and move to the next building 
# by possibly using bricks or ladders.

# While moving from building i to building i+1 (0-indexed),

# If the current building's height is greater than or equal to the next building's height,
# you do not need a ladder or bricks.
# If the current building's height is less than the next building's height, you can either 
# use one ladder or (h[i+1] - h[i]) bricks.
# Return the furthest building index (0-indexed) you can reach if you use the 
# given ladders and bricks optimally.
import heapq

def furthestBuilding(heights, bricks, ladders):
    diffs = []
    nb_buildings = len(heights)
    i = 0
    while i < nb_buildings - 1:
        print(i)
        diff = heights[i + 1] - heights[i]
        if diff > 0:
            print(i)
            heapq.heappush(diffs, diff)
            if len(diffs)  > ladders:
                min_diff = heapq.heappop(diffs)
                if bricks >= min_diff:
                    bricks -= min_diff
                else: 
                    break
        i += 1
    return i

heights = [14,3,19,3]
bricks = 17
ladders = 0

print(furthestBuilding(heights, bricks, ladders))


                

