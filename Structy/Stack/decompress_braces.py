# def decompress_braces(string):
#   stack = []
#   for char in string:
#     if char != '{':
#       if char == '}':
#         stack.append(segment(stack))
#       else:
#         stack.append(char)
#   res = "".join(stack)
#   return res

# def segment(stack):
#   seq = []
#   numbers = "012345679"
#   while stack[-1] not in numbers:
#     char = stack.pop()
#     seq.append(char)
#   number = stack.pop()
#   newseq = seq[::-1]
#   res_part1 = ''.join(newseq)
#   res = res_part1 * int(number)
#   return res

def decompress_braces(string):
  numbers = '12345679'
  stack = []
  for char in string:
    if char in numbers: # Number
      number = int(char)
      stack.append(number)
    elif char == '}':
      segment = ''
      while not isinstance(stack[-1], int): # char within braces
        char = stack.pop()
        segment = char + segment
      number = stack.pop()
      stack.append(segment * number)
    elif char != '{':
      stack.append(char) # Letter
  return ''.join(stack)