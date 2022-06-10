def min_change(amount, coins):
	result = _min_change(amount, coins, {})
	if result == float('inf'):
		return -1
	else:
		return result

def _min_change(amount, coins, memo):
	if amount in memo:
		return memo[amount]

	if amount < 0:
		return float('inf')

	if amount == 0:
		return 0

	min_coin = float('inf')

	for coin in coins:
		change = 1 + _min_change(amount - coin, coins, memo)
		if change < min_coin:
			min_coin = change

	memo[amount] = min_coin
	return min_coin
