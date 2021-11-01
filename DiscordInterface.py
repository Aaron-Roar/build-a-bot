import discord
import command_parser as command
import MedaData as MedaData
import language_parse as LP



class MyClient(discord.Client):
        
    #async def transmit(self, message, meda_data):
      
    def isSelf(self, user):
      if(user.bot):
        return True
      else:
        return False

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        self.bot_user = discord.client

    async def transmit(self, data, meda_data):
        await meda_data.channel.send(data)

    async def on_message(self, message):
        meda_data = MedaData.getMedaData(message)

        if(self.isSelf(meda_data.user) == False):
          if(meda_data.content_type == 1):
            user_command = MedaData.removeSlash(str    (meda_data.content))
            value = command.runCommand(user_command)
          
            await self.transmit(value, meda_data)
            print("Value: " + str(value))
        
          else:
            values = ""
            values += LP.evaluate_phrase(str(meda_data.content))
            if(values == ""):
              print("no language cases")
            else:
              print("Values: " + values)
              await self.transmit(values, meda_data)
        else:
            print("Bot sent a message")