def nesting_score(string):
  stack = [0]

  for char in string:
    if char == '[':
      stack.append(0)
    else:
      popped = stack.pop()
      if popped == 0:
        stack[-1] += 1
      else:
        stack[-1] += popped * 2

  return stack[0]