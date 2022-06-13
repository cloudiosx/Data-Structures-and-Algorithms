def subsets(elements):
	if len(elements) == 0:
		return [[]]

	first_ele = elements[0] # a
	subset_without_first = subsets(elements[1:])

# [
#   [],
#   [ 'c' ],
#   [ 'b' ],
#   [ 'b', 'c' ],
# ]

	subset_with_first = []
	for ele in subset_without_first:
		subset_with_first.append([first_ele, *ele])

# [
#   [ 'a' ],
#   [ 'a', 'c' ],
#   [ 'a', 'b' ],
#   [ 'a', 'b', 'c' ]
# ]

	return subset_without_first + subset_with_first

subsets(['a', 'b', 'c']) # ->
# [
#   [],
#   [ 'c' ],
#   [ 'b' ],
#   [ 'b', 'c' ],
#   [ 'a' ],
#   [ 'a', 'c' ],
#   [ 'a', 'b' ],
#   [ 'a', 'b', 'c' ]
# ]