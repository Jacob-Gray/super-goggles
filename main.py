import getpass
import logging
import logging.handlers
import os
import random
import sys
import bot
import user
import time

import ChatExchange.chatexchange.client
import ChatExchange.chatexchange.events

client = None
my = None
host_id = ""

logger = logging.getLogger(__name__)


def main():
  
  global client
  global my
  global host_id
  
  host_id = "stackoverflow.com"
  setup_logging()
  
  if 'ChatExchangeU' in os.environ:
    email = os.environ['ChatExchangeU']
  else:
    email = raw_input(">> What is your email? \n")
  
  if 'ChatExchangeP' in os.environ:
    password = os.environ['ChatExchangeP']
  else:
    password = raw_input(">> What is your password? \n")
    
  client = user.user(host_id, email, password);
  my = client.get_me();
  
  room = bot.join(client, 111583, on_message)
  
  if "first_start" in sys.argv:
    commit = os.popen('git log --pretty=format:"%h" -n 1').read()
    room.send_message("Super Goggles is up! Running on commit: [`" + commit + "`](https://github.com/Jacob-Gray/super-goggles/commit/"+commit+")")
  

  
  while True:
    message = raw_input("<< ")
    if message == "die":
      room.send_message("Shutting down...")
      time.sleep(0.4)
      break
    else:
      room.send_message(message)

  os._exit(6)



def on_message(message, client):
  
  priv_commands = ["pull","join","leave","priv"]
  
  S_user_id = str(message.user.id)
  S_room_id = str(message.room.id)
  
  user_id = message.user.id
  room_id = message.room.id
  
  if not isinstance(message, ChatExchange.chatexchange.events.MessagePosted):
    # Ignore non-message_posted events.
    logger.debug("event: %r", message)
    return

  if message.content.startswith('sg '):
    
    command = message.content.split()[1]
    
    if user.privileged(S_user_id, S_room_id, host_id) and command in priv_commands:
      
      if command == "pull":
        message.message.reply("`git pull` from [`https://github.com/Jacob-Gray/super-goggles/`](https://github.com/Jacob-Gray/super-goggles/)")
        os._exit(3)
        
      elif command == "join":
        
        room_id = int(message.content.split()[2])
        
        r = bot.join(client, room_id, on_message)
        user.setPrivileged(S_user_id, S_message_id, host_id)
        
        r.send_message("Hey guys, I joined at request of ["+message.user.name+"](http://stackoverflow.com/users/"+str(message.user.id)+")")
        message.message.reply("I am now listening in room [`#"+str(room_id)+"`](http://chat.stackoverflow.com/rooms/"+str(room_id)+")")
      
      elif command == "leave":
        message.message.reply("Okay, I'm leaving.")
        bot.leave(message.room.id)
        
      elif command == "priv":
        tmp_user = message.content.split()[2]
        priv = user.setPrivileged(user, S_message_id, host_id)
        if priv == 0:
          message.message.reply("User [`#"+user+"`](http://"+host_id+"/users/"+user+") is now a privileged user in this room")
          
        elif priv == 1:
          message.message.reply("User [`#"+user+"`](http://"+host_id+"/users/"+user+") is already a privileged user in this room")
          
      else:
        message.message.reply("`"+message.content+"` isn't a valid command.")
    
    else:
      message.message.reply("You aren't a privileged users. You can request access with `sg request priv`.");

    

#Yay, logging!
 
def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger.setLevel(logging.DEBUG)

    # In addition to the basic stderr logging configured globally
    # above, we'll use a log file for chatexchange.client.
    wrapper_logger = logging.getLogger('ChatExchange.chatexchange.client')
    wrapper_handler = logging.handlers.TimedRotatingFileHandler(
        filename='client.log',
        when='midnight', delay=True, utc=True, backupCount=7,
    )
    wrapper_handler.setFormatter(logging.Formatter(
        "%(asctime)s: %(levelname)s: %(threadName)s: %(message)s"
    ))
    wrapper_logger.addHandler(wrapper_handler)

if __name__ == '__main__':
    main()
