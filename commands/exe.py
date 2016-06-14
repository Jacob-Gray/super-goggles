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
