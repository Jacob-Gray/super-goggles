#bot/commands - Guidelines
The command dictionary is stored in `/commands/exe.py` and should be used like:
```
import commands

commands.exe((String) Command Name, (Object) Message, (Object Client));
```
**Adding a command:**
To add a command, create a file in the command directory, with the filename as the desired command name. The function that is called when running the command should be called `exe`, and take the `Message` and `Client` parameters.

An example is below:

```
# example.py

def exe(message, client):
	message.message.reply("This is an example command!")
```
