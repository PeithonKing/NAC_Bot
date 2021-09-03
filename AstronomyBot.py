import os
from discord.ext import commands
# from keep_alive import keep_alive

client = commands.Bot(command_prefix = "/")

@client.event
async def on_ready():
	print("Bot is Ready")


# All the code here


client.run(os.getenv("DiscordBotToken"))