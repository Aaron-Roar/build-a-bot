import Packages
from CommandParser import command_parser as parser

def evaluate_phrase(sentence):
  words = parser.parseWords(str(sentence))
  response = ""
  new_response = str()
  features = [] 

  for i in searchWords(words):
    features.append(i)

  for i in features:
    output = i.setup(words)
    print(output)
    response += output
    response += "\n"
    new_response += response
  #return here to output a list of the responses
  return new_response

def searchWords(words):
  match_list = []

  for i in words:
    if i in Packages.LanguageCatch:
      match_list.append(checkDict(i))

  return match_list

def checkDict(word):
    obj_type = Packages.LanguageCatch[word]
    return obj_type



# funtion out> ooof lmao 