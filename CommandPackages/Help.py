import Variables

def format(text, wrap_num):
  def addLine(string, num):
    i = int(0)
    while(i < num):
      string += "_"
      i += 1
  
  def addText(formatted_text, text, num):
    char_count = int(0)
    i = int(0)

    while(char_count < len(text)):
      formatted_text += "|"
      while(i < num):
        formatted_text += text[char_count]
        char_count += 1
        i += 1
      formatted_text += "\n"

  formatted_string = str()
  addLine(formatted_string, wrap_num)
  addText(formatted_string, text, wrap_num)
  addLine(formatted_string)

  return formatted_string

  
  




class Help():
  def Help(commands):

    thing = f"""
    ```python
    'Need Help understanding smooth brain?
    its a discord bot not really hard to understand'
    ___________________________________________________________________________________
    |'    {Variables.command_token}    ' is your command prefix you                    |
    | type that into the                                                               |
    | appropriate discord text channel                                                 |
    | before a message if u wanna use a command                                        ||                                                                                  ||__________________________________________________________________________________|
    
    
    
    
    
    
    
    
    
    
    
    
    If your internet handle goes by {Variables.friends} 
    then its your shitty china pc why the bot isnt working 
    
    
    ```
    """

    return thing


  dict = {
    "Help":Help,
  }


class Commands():
  def Commands(commands):
    CommandHelp = """
    ```python
    'Alright so our bot confuses you eh?

    /About = info about the devs and testing

    /Help = helpful info about the bot

    /Math(add)(,)(subtract)(,)(Mulitiply) = 
    input your math problem and hopfully 
    a computer can figure it out 

    /WordPlay(backwords) = to output a word 
    in reverse 

    /AsciiArt = for fun clip art spam 
    ```
    """
    
    return CommandHelp 


  dict = {
    "Commands":Commands,
  }



class About():
  def About(commands):
    
    ABOUTME = """
    ```
     Built by !Rain#6933
     Questioned by Rymink#0362
     stolen from https://github.com/


     Accounts effected by ddos tool
     1). MiniMerz#1352(RIP)
     2). N0t0r10usB1ack#9651(RIP)
     ```
    """
    return ABOUTME

  dict = {
    "About":About,
  }
  
class China():
  def China(commands):
    Number1 = """
    ```python
    '
 _____  _      _                   _  _    __  
/  __ \| |    (_)                _| || |_ /  | 
| /  \/| |__   _  _ __    __ _  |_  __  _|`| | 
| |    | '_ \ | || '_ \  / _` |  _| || |_  | | 
| \__/\| | | || || | | || (_| | |_  __  _|_| |_
 \____/|_| |_||_||_| |_| \__,_|   |_||_|  \___/' 
 """ 
    return Number1 
 
  dict = {
    "China":China,
  }