# 1137. N-th Tribonacci Number
def tribonacci(n):
    tribonacciNumbers = [0, 1, 1]
    for i in range(3, n + 1):
        tribonacciNumbers.append(
            tribonacciNumbers[i - 1]
            + tribonacciNumbers[i - 2]
            + tribonacciNumbers[i - 3]
        )

    return tribonacciNumbers[n]
