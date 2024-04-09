# 1094. Car Pooling
def carPooling(trips, capacity):
    numbPassengers = [0]*(1001)
    for trip in trips:
        numbPassengers[trip[1]] += trip[0]
        numbPassengers[trip[2]] -= trip[0]
    if numbPassengers[0] > capacity:
        return False
    
    for i in range(1, len(numbPassengers)):
        numbPassengers[i] += numbPassengers[i - 1]
        if numbPassengers[i] > capacity:
            return False
    return True
