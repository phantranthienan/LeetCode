def change(amount, coins):
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1
    for coin in coins:
        for val in range(amount + 1):
            print(type(val))
            if (val >= coin):
                dp[val] += dp[val - coin]
    return dp[-1]

print(change(5, [1, 2, 5]))

