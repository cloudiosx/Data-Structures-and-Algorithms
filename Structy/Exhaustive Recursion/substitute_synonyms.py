def substitute_synonyms(sentence, synonyms):
  words = sentence.split()
  all_possibilities = generate(words, synonyms)
  res = []
  for possibility in all_possibilities:
    res.append(' '.join(possibility))
  return res

def generate(words, synonyms):
  if len(words) == 0:
    return [[]]

  first_word = words[0]
  remaining_words = words[1:]
  remaining_possibilities = generate(remaining_words, synonyms)

  if first_word in synonyms:
    res = []
    for synonym in synonyms[first_word]:
      for possibility in remaining_possibilities:
        res.append([synonym, *possibility])
    return res
  else:
    res = []
    for possibility in remaining_possibilities:
        res.append([first_word, *possibility])
    return res