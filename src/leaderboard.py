import discord
import os 
import mysql.connector
import logutils as lu
from db.connections import dbconnections as dbcon 

async def call(d_message,msg):
    proc = os.path.basename(__file__)
    dm = False
    personal = False
    delim = 10
    if('-dm' in msg):
        dm = True
    if('-p' in msg):
        personal = True
    if('-c' in msg):
        index = msg.index('-c') + 1
        try:
            delim = int(msg[index])
        except (ValueError,IndexError) as err:
            print(f"User {d_message.author} passed invalid number {msg[len(msg)-1]}.")
            delim = 10 #sanity
            logentry= f'Invalid leaderboard count delimiter sent by user {d_message.author.id}. PARAMS dm:{dm}, personal:{personal} msg{msg}'
            lu.submitlog(lu.Severity.NOTIFICATION.value,lu.Issuer.Python.value,proc,logentry)
    try:
        conn = mysql.connector.connect(user=dbcon.user,password=dbcon.password,host=dbcon.host,database=dbcon.db)
        cur = conn.cursor()
        personid = None 
        if(personal):
            personid = d_message.author.id
        params = [personid, delim]
        cur.callproc('leaderboard_get',params)
        conn.commit()
        reply = discord.Embed(title="Post leaderboard", color=0xc73228)
        place = 1

        for result in cur.stored_results():
            p = result.fetchall()
        for i in range(len(p)):
            name = p[i][0]
            postcount = str(p[i][1])
            fv = name + " " + str(postcount) + " posts" 
            if(not personal):
                reply.add_field(name=place,value=fv,inline=False)
            else:
                reply.add_field(name="Your postcount",value=fv,inline=False)
            place += 1


        if(dm):
            await d_message.author.send(embed=reply)
        else:
            await d_message.channel.send(embed=reply)
            logentry= f'Succesfully replied to {d_message.author.id}. PARAMS dm:{dm}, personal:{personal} msg{msg}'
            lu.submitlog(lu.Severity.INFORMATION.value,lu.Issuer.Python.value,proc,logentry)
    except mysql.connector.Error as error:
        print(f'Query error:{err}')
        logentry= f'Error in replying to {d_message.author.id}. PARAMS dm:{dm}, personal:{personal} msg{msg}'
        lu.submitilog(lu.Severity.ERROR.value,lu.Issuer.Python.value,proc,logentry)
     
    finally:
        if(conn.is_connected()):
            cur.close()
            conn.close()

