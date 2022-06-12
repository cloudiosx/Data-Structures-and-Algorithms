def befitting_brackets(string):
  stack = []

  symbols = {
    "(": ")",
    "[": "]",
    "{": "}"
  }

  for char in string:
    if char in symbols:
      stack.append(symbols[char])
    else:
      print(symbols[char])
      if stack and stack[-1] == symbols[char]:
        stack.pop()
      else:
        return False

  return len(stack) == 0

befitting_brackets('(){}[](())') # -> True