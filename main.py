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


logger = logging.getLogger(__name__)

def main():
  setup_logging()
  
  if 'ChatExchangeU' in os.environ:
    email = os.environ['ChatExchangeU']
  else:
    email = raw_input(">> What is your email? \n")
  
  if 'ChatExchangeP' in os.environ:
    password = os.environ['ChatExchangeP']
  else:
    password = raw_input(">> What is your password? \n")
    
  client = user.user("stackoverflow.com",email,password);
  
  room = client.get_room(111583)
  room.join()
  
  if "first_start" in sys.argv:
    commit = os.popen('git log --pretty=format:"%h" -n 1').read()
    room.send_message("Super-goggles is up! Running on commit: [`" + commit + "`](https://github.com/Jacob-Gray/super-goggles/commit/"+commit+")")
  
  room.watch(on_message)
  
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
  if not isinstance(message, ChatExchange.chatexchange.events.MessagePosted):
    # Ignore non-message_posted events.
    logger.debug("event: %r", message)
    return

  if message.content.startswith('sg'):
    if message.content.split()[:1] == "pull":
      message.message.reply("`git pull` from [`https://github.com/Jacob-Gray/super-goggles/`](https://github.com/Jacob-Gray/super-goggles/)")
      os._exit(3)
    else:
      message.message.reply("`"+message.content+"` isn't a valid command.")

    

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
