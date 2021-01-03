import os
import dbconnections as dbcon
import messageparser
import discord
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

async def increment_leaderboard(message):
    try:
        conn = mysql.connector.connect(user=dbcon.user,password=dbcon.password,host=dbcon.host,database=dbcon.db)
        cur = conn.cursor()
        params = [message.author.id, message.author.name] 
        cur.callproc('leaderboard_upd',params)
        conn.commit()
    except mysql.connector.Error as err:
        print(f'{err}')
    finally:
        print(f'{message.author} sent a message, leaderboard incremented for userid {message.author.id}')
        cur.close()
        conn.close()


@client.event
async def on_ready():
    print(f'Bot ready')

@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    else:
        print({message.author.id})
        await increment_leaderboard(message);
        await messageparser.parse_message(message)

client.run(TOKEN)

