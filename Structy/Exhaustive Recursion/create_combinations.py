def create_combinations(items, k):
  if k > len(items):
    return []

  if k == 0:
    return [[]]

  first_element = items[0]
  subset_decrement = create_combinations(items[1:], k - 1)
  subset_without_decrement = create_combinations(items[1:], k)

  subset_with_first = []
  for subset in subset_decrement:
    subset_with_first.append([first_element, *subset])

  return subset_with_first + subset_without_decrement

