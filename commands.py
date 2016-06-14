#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import bot
import user
import main
import difflib


# Define a command as a function, then add it to `command_dict`

# `pull` Command
# required_info: message
# <eg> commands.exe("pull", message)-e.reply('I am a Chat bot, built by [Jacob Gray](http://stackoverflow.com/users/3285730/jacob-gray) for the StackExchange Chats. You can find my source on [Github](https://github.com/Jacob-Gray/super-goggles/), and I am based of the [ChatExchange lib](https://github.com/Manishearth/ChatExchange). You can see my available commands by sending `sg help`.'
                          )





command_dict = {
    'leave': leave,
    'pull': pull,
    'join': join,
    'info': info,
    'about': about,
    '': about,
    'swim': swim,
    }





