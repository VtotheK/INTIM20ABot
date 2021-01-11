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
            return val,True
        except ValueError:
            debugmsg = f"{d.now()}: {tkn} flag was defined but no correct value was supplied by {d_msg.author.id}."
            print(debugmsg)
            lu.submitlog(lu.Severity.NOTIFICATION.value,lu.Issuer.Python.value,callingproc,debugmsg)
            d_msg.channel.send('You defined -{tkn} flag, but you didn''t give me a correct value. Please check the input, or check the correct syntax for getting deadlines by typing ```$bot -h -d```')
            return None,False
    return None,True


async def parsemessage(d_msg,msg):
    personal = False
    dm = False
    userid = None
    proc = os.path.basename(__file__)
    deadlineid,d_tkn = gettoken(msg,'-id')
    if(not d_tkn):
        return
    rowlimit,r_tkn = gettoken(msg,'-c')
    if(not r_tkn):
        return
    if('-p' in msg):
        personal = True
        userid = d_msg.author.id
    if('-dm' in msg):
        dm = True
    try:
        conn = mysql.connector.connect(user=dbcon.user,password=dbcon.password,host=dbcon.host,database=dbcon.db)
        cur = conn.cursor()
        params = [deadlineid,userid,rowlimit]
        cur.callproc('deadlines_get',params)
        conn.commit()
        msg = ""
        for result in cur.stored_results():
            p = result.fetchall()
        for i in range(len(p)):
            msg += f"**Deadline Id**:{p[i][0]}\n**Deadline**: {p[i][6]}\n**Summary**: {p[i][4]}\n-------------------------------------\n"
        if(not dm):
            await d_msg.channel.send(msg)
        else:
            await d_msg.author.send(msg)
        print(f'Succesfully delivered deadlines to user {d_msg.author.id}')
        debugmsg = f'Succesfully sent deadlines to user {d_msg.author.id}, params: dm={dm} personal={personal}'
        lu.submitlog(lu.Severity.INFORMATION.value,lu.Issuer.Python.value,proc,debugmsg)
    except mysql.connector.Error as error: 
        print("{error}")
        debugmsg = f'Failed to send deadlines to user [d_msg.author.id], params: dm={dm} personal={personal}, msg={str(msg), SQL-error:{error}}'
        lu.submitlog(lu.Severity.CRITICALERROR.value,lu.Issuer.Python.value,proc,debugmsg)
    
