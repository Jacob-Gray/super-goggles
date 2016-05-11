import getpass
import logging
import logging.handlers
import os
import random
import sys
import bot
import user

import chatexchange.client
import chatexchange.events


logger = logging.getLogger(__name__)

def main():
  setup_logging()
  email = raw_input(">> What is your email? \n")
  pswd = raw_input(">> What is your password? \n")
  client = user.user("stackoverflow.com",email,pswd);
  room = client.get_room(111583)
  room.join()
  room.watch(on_message)
  
  print "(You are now in room #%s on %s.)" % (room_id, host_id)
  
  room.send_message("Bot Started")
  while True:
      message = raw_input("<< ")
      room.send_message(message)

  client.logout()


def on_message(message, client):
    if not isinstance(message, chatexchange.events.MessagePosted):
        # Ignore non-message_posted events.
        logger.debug("event: %r", message)
        return

    print ""
    print ">> (%s) %s" % (message.user.name, message.content)
    if message.content.startswith('!!/random'):
        print message
        print "Spawning thread"
        message.message.reply(str(random.random()))

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