import logutils as lu
from db.connections import dbconnections as dbcon
import discord
import mysql.connector
import os
from datetime import datetime as d

def gettoken(msg,tkn):
    if(tkn in msg):
        index = msg.index(tkn,0) + 1
        try:
            val = int(msg[index])
            if(tkn == '-l' and (val > 10 or val < 1)):
                raise ValueError
            return str(val),True
        except ValueError:
            debugmsg = f"{d.now()}: {tkn} flag was defined but no correct value was supplied by {d_msg.author.id}."
            print(debugmsg)
            lu.submitlog(lu.Severity.NOTIFICATION.value,lu.Issuer.Python.value,callingproc,debugmsg)
            d_msg.channel.send('You defined -{tkn} flag, but you didn''t give me a correct value. Please check the input, or check the correct syntax for getting deadlines by typing ```$bot -h -d```')
            return None,False
    return None,True


async def parsemessage(d_msg,msg):
    callingproc = os.path.basename(__file__)
    deadlineid,d_tkn = gettoken(msg,'-id')
    if(not d_tkn):
        return
    rowlimit,r_tkn = gettoken(msg,'-r')
    if(not r_tkn):
        return
    userid = None
    if('-p' in msg):
        userid = d_msg.author.id
    try:
        limit = 10
        conn = mysql.connector.connect(user=dbcon.user,password=dbcon.password,host=dbcon.host,database=dbcon.db)
        cur = conn.cursor()
        params = [deadlineid,userid,limit]
        cur.callproc('deadlines_get',params)
        conn.commit()
        for result in cur.stored_results():
            p = result.fetchall()
        for i in range(len(p)):
            msg = f"```Deadline id:{p[i][0]}\nSummary: {p[i][4]}\nDeadline: {p[i][6]}\n```"
            await d_msg.channel.send(msg)
    except mysql.connector.Error as error: 
        print("{error}")
