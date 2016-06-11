#!/usr/bin/python
# -*- coding: utf-8 -*-

import getpass
import logging
import logging.handlers
import os
import random
import sys
import bot
import user
import commands
import time

import ChatExchange.chatexchange.client
import ChatExchange.chatexchange.events

client = None
my = None
host_id = 'stackoverflow.com'

logger = logging.getLogger(__name__)


def main():

    global client
    global my
    global host_id

    host_id = 'stackoverflow.com'
    setup_logging()

    if 'ChatExchangeU' in os.environ:
        email = os.environ['ChatExchangeU']
    else:
        email = raw_input('>> What is your email? \n')

    if 'ChatExchangeP' in os.environ:
        password = os.environ['ChatExchangeP']
    else:
        password = raw_input('>> What is your password? \n')

    client = user.user(host_id, email, password)
    my = client.get_me()

    room = bot.join(client, 113461, chat_event)

    if 'first_start' in sys.argv:
        commit = os.popen('git log --pretty=format:"%h" -n 1').read()
        room.send_message('Super Goggles is up! Running on commit: [`'
                          + commit
                          + '`](https://github.com/Jacob-Gray/super-goggles/commit/'
                           + commit + ')')

    while True:
        message = raw_input('<< ')
        if message == 'die':
            room.send_message('Shutting down...')
            time.sleep(0.4)
            break
        else:
            room.send_message(message)

    os._exit(6)


def chat_event(message, client):
    if not isinstance(message,
                      ChatExchange.chatexchange.events.MessagePosted):

    # Ignore non-message_posted events.

        logger.debug('event: %r', message)
        return
    if message.content.startswith('sg '):
        on_command(message, client)


def on_command(message, client):
    command = message.content.split()[1]
    executed = commands.exe(command, message, client)
    if not executed:
        message.message.reply('`' + command + "` isn't a valid command");
	else:
		couldbe = executed[0]
		message.message.reply("Did you mean "+couldbe)


# Yay, logging!

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger.setLevel(logging.DEBUG)

    # In addition to the basic stderr logging configured globally
    # above, we'll use a log file for chatexchange.client.

    wrapper_logger = \
        logging.getLogger('ChatExchange.chatexchange.client')
    wrapper_handler = \
        logging.handlers.TimedRotatingFileHandler(filename='client.log'
            , when='midnight', delay=True, utc=True, backupCount=7)
    wrapper_handler.setFormatter(logging.Formatter('%(asctime)s: %(levelname)s: %(threadName)s: %(message)s'
                                 ))
    wrapper_logger.addHandler(wrapper_handler)


if __name__ == '__main__':
    main()
