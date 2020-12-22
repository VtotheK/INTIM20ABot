import os
import messageparser
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f"name of the guild is: kurwa")

@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    else:
        await messageparser.parse_message(message)

client.run(TOKEN)
