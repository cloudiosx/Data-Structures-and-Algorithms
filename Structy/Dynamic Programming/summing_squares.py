from math import sqrt, floor
def summing_squares(n):
  return _summing_squares(n, {})

def _summing_squares(n, memo):
  if n in memo:
    return memo[n]

  if n == 0:
    return 0

  min_squares = float('inf')
  for i in range(1, floor(sqrt(n)) + 1):
    square = i * i
    num_squares = 1 + _summing_squares(n - square, memo)
    min_squares = min(num_squares, min_squares)

  memo[n] = min_squares
  return memo[n]
