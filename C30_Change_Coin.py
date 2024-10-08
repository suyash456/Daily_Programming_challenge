def Coin_Change(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Test Case 1
coins = [1, 2, 5]
amount = 11
print(Coin_Change(amount, coins))

# Test Case 1
coins = [2]
amount = 3
print(Coin_Change(amount, coins))

# Test Case 1
coins = [1]
amount = 0
print(Coin_Change(amount, coins))
