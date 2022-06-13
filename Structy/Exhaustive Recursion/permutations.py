def permutations(items):
  if len(items) == 0:
    return [[]]

  first_ele = items[0]
  subset_without_first = permutations(items[1:])
  res = []
  for perm in subset_without_first:
    for i in range(len(perm) + 1):
      res.append(perm[:i] + [first_ele] + perm[i:])
  return res

