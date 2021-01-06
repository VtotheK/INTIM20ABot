import os
import dbconnections as dbcon
import messageparser
import discord
import logutils as lu
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

async def increment_leaderboard(message):
    callingproc = os.path.basename(__file__)
    try:
        conn = mysql.connector.connect(user=dbcon.user,password=dbcon.password,host=dbcon.host,database=dbcon.db)
        cur = conn.cursor()
        params = [message.author.id, message.author.name] 
        cur.callproc('leaderboard_upd',params)
        conn.commit()
        print(f'{message.author} sent a message, leaderboard incremented for userid {message.author.id}')
        msg = f'Succesfully incremented leaderboard for user {message.author.id}.'
        lu.submitlog(lu.Severity.INFORMATION.value,lu.Issuer.Python.value,callingproc,msg)
    except mysql.connector.Error as err:
        print(f'{err}')
        msg = f'Error incrementing leaderboard for user {message.author.id}.'
        lu.submitlog(lu.Severity.ERROR.value,lu.Issuer.Python.value,callingproc,msg)

    finally:
        if(conn.is_connected()):
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

