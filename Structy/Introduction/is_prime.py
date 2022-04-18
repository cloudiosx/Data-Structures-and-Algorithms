import math
def is_prime(n):
  sqrtNumber = math.sqrt(n)
  if n == 1:
    return False
  for num in range(2, int(sqrtNumber) + 1):
    print(num)
    if n % num == 0:
      return False
  return True

# Solution for O(n) time

def is_prime(n):
  if n < 2:
    return False
  
  for i in range(2, n):
    if n % i == 0:
      return False
  
  return True

# Solution for O(sqrt(n)) time

def is_prime(n):
  if n < 2:
    return False
  
  for i in range(2, math.floor(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  
  return True

