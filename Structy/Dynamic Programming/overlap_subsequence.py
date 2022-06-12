def overlap_subsequence(string_1, string_2):
  return _overlap_subsequence(string_1, string_2, 0, 0, len(string_1) - 1, len(string_2) - 1, {})

def _overlap_subsequence(string_1, string_2, start_1, start_2, end_1, end_2, memo):
  key = (start_1, start_2, end_1, end_2)
  if key in memo:
    return memo[key]

  if start_1 > end_1 or start_2 > end_2:
    return 0

  if string_1[start_1] == string_2[start_2]:
    memo[key] = 1 + _overlap_subsequence(string_1, string_2, start_1 + 1, start_2 + 1, end_1, end_2, memo)
  else:
    memo[key] =  max(
      _overlap_subsequence(string_1, string_2, start_1 + 1, start_2, end_1, end_2, memo),
      _overlap_subsequence(string_1, string_2, start_1, start_2 + 1, end_1, end_2, memo)
      )

  return memo[key]