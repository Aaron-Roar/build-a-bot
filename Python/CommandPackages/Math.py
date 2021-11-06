#A collection of math functions
class Math():
  def add(commands):
    return (int(commands[2]) + int(commands[3]))
  
  def subtract(commands):
    return (int(commands[2]) - int(commands[3]))

  dict = {
    "add":add,
    "subtract":subtract,
  }