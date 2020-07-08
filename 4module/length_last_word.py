def length_of_last_word(words):
  return len(words.split()[-1]) if len(words.split())>1 else len(words)