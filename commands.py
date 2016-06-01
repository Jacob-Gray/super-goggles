import os
import bot
import user
import main

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

def info(message):
  infotype = str(message.content.split()[2])
  
  def users():
    print "Okay"
    
  def rooms():
    out = "Super Goggles is currently listening in room"
    bl = len(bot.rooms)
    
    if bl > 1:
      out += "s"
    
    for i in bot.rooms:
      out += ", " + str(i)
    
    outarray = list(out)
    li = out.rindex(',')
    outarray[li] = "&"
    message.message.reply("".join(out))
      
      
      
    
  information = {"rooms":rooms,"users":users}
  
  if infotype in information:
    information[infotype]()
  else:
    message.message.reply("`"+infotype+"` isn't a valid info type")

#`join` Command
#required_info: message
#<eg> commands.exe("join", message)
def join(message):
    tmp_room = str(message.content.split()[2])
    r = bot.join(user.globalClient, int(tmp_room), main.on_message)
    r.send_message("Hey guys, I joined at request of ["+message.user.name+"](http://stackoverflow.com/users/"+str(message.user.id)+")")
    message.message.reply("I am now listening in room [`#"+tmp_room+"`](http://chat.stackoverflow.com/rooms/"+tmp_room+")")

command_dict = {"leave":leave,"pull":pull,"join":join,"info":info}

#Execute commands
#Input: (command name, command input object)
#<eg> commands.exe("join",message)
#Output: True or False
#True means the command was executed, False means it doesn't exist
def exe(command, required_info):
  if command in command_dict:
    command_dict[command](required_info)
    return True
  else:
    return False
  
