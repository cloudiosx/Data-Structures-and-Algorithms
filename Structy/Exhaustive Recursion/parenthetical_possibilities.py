def parenthetical_possibilities(s):
  if len(s) == 0:
  	return ['']

  choices, remainder = get_choices(s)
  all_possilibities = []
  for choice in choices:
  	remainder_possibilities = parenthetical_possibilities(remainder)
  	for string in remainder_possibilities:
  		all_possilibities.append(choice + string)
  return all_possilibities


def get_choices(s):
	if s[0] == '(':
		index_of_close_parentheses = s.index(')')
		return (s[1:index_of_close_parentheses], s[index_of_close_parentheses + 1:])
	else:
		return (s[0], s[1:])

print(parenthetical_possibilities("(qr)ab(stu)c")) # ->
# [ 'qabsc', 'qabtc', 'qabuc', 'rabsc', 'rabtc', 'rabuc' ]