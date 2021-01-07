import logutils as lu
from db.connections import dbconnections as dbcon
import discord
import mysql.connector
import os
from datetime import datetime as d

async def parsemessage(d_msg,msg):
    callingproc = os.path.basename(__file__)
    if('-id' in msg):
        ind = index('-id',0) + 1
        try:
            val = int(msg[ind])
        except ValueError:
            debugmsg = f"{d.now()}: -id flag was defined but no correct id was supplied by {d_msg.author.id}"
            print(debugmsg)
            logutils.submitlog(lu.Severity.NOTIFICATION.value,lu.Issuer.Python.value,callingproc,debugmsg)
            d_msg.channel.send('You defined -id flag but you didn''t give me a correct id. Please check the input, or check the correct syntax for getting deadlines by typing ```$bot -h -d```')
            return
