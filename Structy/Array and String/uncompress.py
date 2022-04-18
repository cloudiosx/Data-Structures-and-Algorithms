# Time complexity: O(nm) | Space complexity: O(nm)
def uncompress(s):
  numbers = '0123456789'
  result = []
  i = 0
  j = 0
  
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      num = int(s[i:j])
      result.append(s[j] * num)
      j += 1
      i = j
  
  return ''.join(result)

# Time complexity: O(n^2m) | Space complexity: O(n^2m)
def uncompress(s):
  numbers = '0123456789'
  result = ''
  i = 0
  j = 0
  
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      num = int(s[i:j])
      result += s[j] * num
      j += 1
      i = j
  
  return result