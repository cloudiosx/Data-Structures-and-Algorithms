def create_combinations(items, k):
  list_num = []
  count = 0
  for num in items:
    if count == k:
      break
    list_num.append(num)
    count += 1
  print(list_num)


# def _create_combinations(items, k):

create_combinations(["a", "b", "c"], 2); # ->
# [
#   [ 'a', 'b' ],
#   [ 'a', 'c' ],
#   [ 'b', 'c' ]
# ]