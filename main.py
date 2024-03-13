import timeit

def find_coins_greedy(amount, coins):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount, coins):
    dp = [0] + [float('inf')]*amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    result = {}
    while amount > 0:
        for coin in coins:
            if amount - coin >= 0 and dp[amount] == dp[amount - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                amount -= coin
                break
                
    return result


coins = [50, 25, 10, 5, 2, 1]
amount = 123

greedy_time = timeit.timeit('find_coins_greedy(123, [50, 25, 10, 5, 2, 1])', globals=globals(), number=1000)
dp_time = timeit.timeit('find_min_coins(123, [50, 25, 10, 5, 2, 1])', globals=globals(), number=1000)

print(f"Greedy algorithm time: {greedy_time}")

print(f"Dynamic programming time: {dp_time}")