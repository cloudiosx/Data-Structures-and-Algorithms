from math import floor
def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, i, memo):
  key = (amount, i)
  if key in memo:
    return memo[key]

  if amount == 0:
    return 1

  if i == len(coins):
    return 0

  coin = coins[i]

  totalSumOfWays = 0
  for qty in range(0, floor(amount / coin) + 1):
    remainder = amount - (coin * qty)
    totalSumOfWays += _counting_change(remainder, coins, i + 1, memo)

  memo[key] = totalSumOfWays
  return memo[key]