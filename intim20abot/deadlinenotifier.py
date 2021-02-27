import os
import discord
from discord.utils import get
from dotenv import load_dotenv
from db.connections import dbconnections as dbcon


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot ready')
    channel = client.get_channel(790692856255742028)
    await channel.send("hello from other script")
    await channel.send("leaving")
    await client.close()
#this works now

client.run(TOKEN)

