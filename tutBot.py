import os, discord
from discord.ext.commands import Bot

# We'll need to substitute the Prefix for an Enviroment Variable
BOT_PREFIX = os.environ['prefix']  # -Prfix is need to declare a Command in discord ex: !pizza "!" being the Prefix
TOKEN = os.environ['token']  # The token is also substituted for security reasons

client = Bot(command_prefix=BOT_PREFIX)


# this is an event which is triggered when something happens in Discord
# in this case on_ready() is called when the bot logs on
# you can checkthe Discord API Documentaion for more event Functions
# here: https://discordapp.com/developers

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="--Insert-Game-name-here--"))


# below this line you can put custom Functions

# This tell the Interpreter that this function is a command for discord
@client.command(name="Command")  # 'name' is literaly the name of the command
async def command():  # commands can also take paramenters this example takes none
    await client.say(""+"This is an example of a Command Function")



client.run(TOKEN)