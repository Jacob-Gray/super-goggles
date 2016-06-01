import os
import bot
import user

#Define a command as a function, then add it to `command_dict`

#`pull` Command
#required_info: message
#<eg> commands.exe("pull", message)
def pull(message):
  message.message.reply("`git pull` from [`https://github.com/Jacob-Gray/super-goggles/`](https://github.com/Jacob-Gray/super-goggles/)")
  os._exit(3)

#`leave` Command
#required_info: message
#<eg> commands.exe("leave", message)
def leave(message):
  message.message.reply("Okay, I'm leaving.")
  bot.leave(message.room.id)


command_dict = {"join":join,"leave":leave,"pull":pull}

#Execute commands
#Input: (command name, command input object)
#<eg> commands.exe("join",[Object])
#Output: True or False
#True means the command was executed, False means it doesn't exist
def exe(command, required_info):
  if command in command_dict:
    command_dict[command](required_info)
    return True
  else:
    return False
  
