def Fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# Test case 1
n = 5
print(Fibonacci(n))

# Test case 1
n = 10
print(Fibonacci(n))

# Test case 1
n = 0
print(Fibonacci(n))

# Test case 1
n = 1000
print(Fibonacci(n))
