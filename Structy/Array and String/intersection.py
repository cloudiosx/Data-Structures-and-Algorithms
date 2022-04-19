# Time complexity: O(n + m) | Space complexity: O(n)
def intersection(a, b):
	items_set = set(a)
  return [ ele for ele in b if ele in items_set ]

def intersection(a, b):
	result = []
	items_set = set()

	for item in a:
		items_set.add(item)

	for ele in b:
		if ele in items_set:
			result.append(ele)

	return result

# Time complexity: O(n * m) | Space complexity: O(min(n, m))
def intersection(a, b):
  result = []
  
  for item in a:
    if item in b: 
      result.append(item)
  
  return result

