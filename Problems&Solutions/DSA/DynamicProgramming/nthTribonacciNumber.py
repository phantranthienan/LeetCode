# 1137. N-th Tribonacci Number
# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

def tribonacci(n):
    tribonacciNumbers = [0, 1, 1]
    for i in range(3, n):
        tribonacciNumbers.append(tribonacciNumbers[i] + tribonacciNumbers[i - 1] + tribonacciNumbers[i - 2])
    
    return tribonacciNumbers[n]