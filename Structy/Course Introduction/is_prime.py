import math
def is_prime(n):
  sqrtNumber = math.sqrt(n)
  if n == 1:
    return False
  for num in range(2, int(sqrtNumber + 1)):
    print(num)
    if n % num == 0:
      return False
  return True