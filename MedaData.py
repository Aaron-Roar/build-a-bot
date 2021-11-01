
class MedaData():
  def set(self, message):
    self.channel = message.channel
    self.user = message.author

    self.content = message.content
    self.content_type = messageType(str(self.content))

def getMedaData(message):
  meda_data = MedaData()
  meda_data.set(message)
  return meda_data



def removeSlash(data):
  value = str()
  for i in data:
    if(i != '/'):
      value += i
  return value


def messageType(content):
  if(str(content)[0] == '/'):
    return 1
  else:
    return 2










def printMedaData(message):
  meda_data = getMedaData(message)
  print("User: " + str(meda_data.user))
  print("Channel: " + str(meda_data.channel))
  print("Message: " + str(meda_data.content))
  print("Message Type: " + str(meda_data.content_type))
  print("\n")




