import Packages as Packages

def runCommand(phrase):
  print("Command: " + str(phrase))
  command = parseWords(str(phrase))

  feature = findFeature(command)

  return feature(command)

#Get the next word till white space
def parseWords(phrase):
  phrase += '\n'
  command = []

  word = str()
  for i in phrase:
    if(i == ' ' or i == '\n'):
      command.append(str(word))
      word = ""
    else:
      word += i
  return command



#Look for the object ascociated with the command
def findFeature(commands):
  feature = 5
  package = Packages.PackageDict[commands[0]]
  if(len(commands) == 1):
    feature = package.dict[commands[0]]
  else:
    feature = package.dict[commands[1]]

  return feature











