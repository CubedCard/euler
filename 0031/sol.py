def f(target, coins):
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    
    return dp[target]

money = [1, 2, 5, 10, 20, 50, 100, 200]

print(f(200, money))
