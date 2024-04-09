# 901. Online Stock Span.

class StockSpanner(object):

    def __init__(self):
        self.stockPrices = [0]
        self.stack = []
        self.day = 0

    def next(self, price):
        self.day += 1
        self.stockPrices.append(price)
        while self.stack and self.stockPrices[self.stack[-1]] <= price:
            self.stack.pop()
        
        self.stack.append(self.day)
        
        if (len(self.stack) == 1):
            return self.day 
        else:
            return self.day - self.stack[-2]

class StockSpanner2(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack.pop()[1]
        self.stack.append([price, count])
        return count
        

        




