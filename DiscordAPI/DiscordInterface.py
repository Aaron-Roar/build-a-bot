import discord
from CommandParser import command_parser as command
from DiscordAPI import MedaData as MedaData
from LanguageParser import language_parse as LP



class MyClient(discord.Client):
        
    #async def transmit(self, message, meda_data):
      
    def isSelf(self, user):
      if(user.bot):
        return True
      else:
        return False

    async def on_ready(self):
        print('Bot has logged on as {0}!'.format(self.user))
        self.bot_user = discord.client

    async def transmit(self, data, meda_data):
        print("Bot reply: " + data)
        print("Channel: " + str(meda_data.channel))
        print("In response to: " + str(meda_data.user))
        await meda_data.channel.send(data)

    async def on_message(self, message):
        meda_data = MedaData.getMedaData(message)

        if(self.isSelf(meda_data.user) == False):
          if(meda_data.content_type == 1):
            user_command = MedaData.removeSlash(str    (meda_data.content))
            value = command.runCommand(user_command)
          
            await self.transmit(value, meda_data)
        
          else:
            values = ""
            values += LP.evaluate_phrase(str(meda_data.content))
            if(values == ""):
              print("no language cases")
            else:
              await self.transmit(values, meda_data)
        else:
            print("Ignoring self notification")