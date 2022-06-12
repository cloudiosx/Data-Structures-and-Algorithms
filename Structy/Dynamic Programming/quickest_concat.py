# def quickest_concat(s, words):
#   return _quickest_concat(s, words, 0, [], {})

# def _quickest_concat(s, words, count, array, memo):
#   tup = (s, count)
#   if tup in memo:
#     return memo[tup]

#   if s == "":
#     return count

#   for word in words:
#     if s.startswith(word):
#       suffix = s[len(word):]
#       array.append(_quickest_concat(suffix, words, count + 1, array, memo))

#   if len(array) == 0:
#     memo[tup] = -1
#     return memo[tup]
#   else:
#     memo[tup] = min(array)
#     return memo[tup]

def quickest_concat(s, words):
  res = _quickest_concat(s, words, {})
  if res == float('inf'):
    return -1
  else:
    return res

def _quickest_concat(s, words, memo):
  if s in memo:
    return memo[s]

  if s == "":
    return 0

  min_words = float('inf')
  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      attempt = 1 + _quickest_concat(suffix, words, memo)
      min_words = min(attempt, min_words)

  memo[s] = min_words
  return memo[s]