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
# <eg> commands.exe("pull", message)

def pull(message, client):
    message.message.reply('`git pull` from [`https://github.com/Jacob-Gray/super-goggles/`](https://github.com/Jacob-Gray/super-goggles/)'
                          )
    os._exit(3)


# `leave` Command
# required_info: message
# <eg> commands.exe("leave", message)

def leave(message, client):
    message.message.reply("Okay, I'm leaving.")
    bot.leave(message.room.id)


def info(message, client):
    infotype = \
        str((message.content.split()[2] if len(message.content.split())
            > 2 else ''))

    def users():
        out = 'User'
        userIDs = bot.rooms[message.room.id].get_current_user_ids()
        userNames = bot.rooms[message.room.id].get_current_user_names()
        bl = len(userIDs)

        if bl > 1:
            out += 's'
        ot = 0
        for i in range(bl):
            HostID = main.host_id
            UserName = userNames[i]
            UserID = userIDs[i]
            if ot == 0:
                out += ' '
            elif ot == bl - 1:
                out += ' & '
            else:
                out += ', '

            out += '[%s](http://%s/users/%i)' % (UserName, HostID,
                    UserID)
            ot += 1
        if bl > 1:
            out += ' are '
        else:
            out += ' is '
        out += 'currently in this room'
        message.message.reply(out)

    def rooms():
        out = 'Super Goggles is currently listening in room'
        bl = len(bot.rooms)

        if bl > 1:
            out += 's'
        ot = 0
        for i in bot.rooms:
            RoomID = str(i)
            HostID = main.host_id
            if ot == 0:
                out += ' '
            elif ot == bl - 1:
                out += ' & '
            else:
                out += ', '

            out += '[`#%s`](http://chat.%s/rooms/%s)' % (RoomID,
                    HostID, RoomID)
            ot += 1

        message.message.reply(out)

    information = {'rooms': rooms, 'users': users}

    if infotype in information:
        information[infotype]()
    elif infotype == '':
        message.message.reply('Please enter what you want information about'
                              )
    else:
        message.message.reply('`' + infotype
                              + "` isn't a valid info type")


# `join` Command
# required_info: message
# <eg> commands.exe("join", message)

def join(message, client):
    tmp_room = str(message.content.split()[2])
    r = bot.join(client, int(tmp_room), main.chat_event)
    if r != 0:
        r.send_message('Hey guys, I joined at request of ['
                       + message.user.name + '](http://' + main.host_id
                       + '/users/' + str(message.user.id) + ')')
        message.message.reply('I am now listening in room [`#'
                              + tmp_room + '`](http://chat.'
                              + main.host_id + '/rooms/' + tmp_room
                              + ')')
    else:
        message.message.reply("I'm already in that room")


def about(message, client):
    message.message.reply('I am a Chat bot, built by [Jacob Gray](http://stackoverflow.com/users/3285730/jacob-gray) for the StackExchange Chats. You can find my source on [Github](https://github.com/Jacob-Gray/super-goggles/), and I am based of the [ChatExchange lib](https://github.com/Manishearth/ChatExchange). You can see my available commands by sending `sg help`.'
                          )


command_dict = {
    'leave': leave,
    'pull': pull,
    'join': join,
    'info': info,
    'about': about,
    '': about,
    }


# Execute commands
# Input: (command name, command input object, [Object Client])
# <eg> commands.exe("join",message)
# Output: True or False
# True means the command was executed, False means it doesn't exist

def exe(command, required_info, client):
    if command in command_dict:
        command_dict[command](required_info, client)
        return True
    else:
        close = difflib.get_close_matches(command, command_dict)
        if not close:
            return False
        else:
            return close


