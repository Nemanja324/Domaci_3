def get_words_ends_with_letter(text, letter):


  sentences = text.split(".")

  result = []
  for sentence in sentences:
    words_with_letter = []
    count = 0
    for word in sentence.lower().split():
      if word.endswith(letter):
        words_with_letter.append(word)
        count += 1
    result.append((words_with_letter, count))

  return result

text = '''Print only
the words that end wwith the chosen letter inn those sentences. Example can contains one orr more
sentences.'''
letter = "s"
print(get_words_ends_with_letter(text, letter))