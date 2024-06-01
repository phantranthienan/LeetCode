# 1801. Number of Orders in the Backlog

def getNumberOfBacklogOrders(orders):
    # orders[i] = [price, amount, orderType]
    # Use heapq in python to solve this problem
    # There will be buyBacklog, which store the buy orders, the same as sellBacklog
    # to sort with the heap, we need to store the price and amount in the heap
    # for buyBacklog, we need to sort with the price in descending order => [-price, amount]
    # for sellBacklog, we need to sort with the price in ascending order => [price, amount]

    import heapq
    buyBacklog = []
    sellBacklog = []

    for order in orders:
        if order[2] == 1: #Order is of sell type
            while order[1] > 0 and buyBacklog and -buyBacklog[0][0] >= order[0]:
                if buyBacklog[0][1] >= order[1]:
                    buyBacklog[0][1] -= order[1]
                    order[1] = 0
                else:
                    order[1] -= buyBacklog[0][1]
                    heapq.heappop(buyBacklog)
            if order[1] > 0:
                heapq.heappush(sellBacklog, [order[0], order[1]])
        else: #Order is of buy type
            while order[1] > 0 and sellBacklog and sellBacklog[0][0] <= order[0]:
                if sellBacklog[0][1] >= order[1]:
                    sellBacklog[0][1] -= order[1]
                    order[1] = 0
                else:
                    order[1] -= sellBacklog[0][1]
                    heapq.heappop(sellBacklog)
            if order[1] > 0:
                heapq.heappush(buyBacklog, [-order[0], order[1]])
    
    return sum([order[1] for order in buyBacklog + sellBacklog]) % (10**9 + 7)

orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]

print(getNumberOfBacklogOrders(orders)) #6