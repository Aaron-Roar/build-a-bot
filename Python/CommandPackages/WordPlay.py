#A collection of word functions
class WordPlay():
  def backwords(commands):
    word = []
    for i in commands[2]:
      word.insert(0, i)
    return word
  
  dict = {
    "Backwords":backwords,
  }