import discord
import os 
import mysql.connector
import dbconnections as dbcon


async def call(d_message,msg):
    dm = False
    personal = False
    delim = 10
    if('-dm' in msg):
        dm = True
    if('-p' in msg):
        personal = True
    try:
        delim = int(msg[len(msg) - 1])
    except ValueError as ve:
        print(f"User {d_message.author} passed invalid number {msg[len(msg)-1]}.")
        delim = 10 #sanity
    try:
        conn = mysql.connector.connect(user=dbcon.p_user,password=dbcon.p_password,host=dbcon.p_host,database=dbcon.p_db)
        cur = conn.cursor()
        personid = None 
        if(personal):
            personid = d_message.author.id
        params = [personid, delim]
        cur.callproc('Leaderboard_Get',params)
        conn.commit()
        reply = discord.Embed(title="Post leaderboard", color=0xc73228)
        place = 1

        for result in cur.stored_results():
            p = result.fetchall()

        for i in range(len(p)):
            name = p[i][0]
            postcount = str(p[i][1])
            fv = name + str(postcount) + " posts" 
            reply.add_field(name=place,value=fv,inline=False)
            place += 1

        if(dm):
            await d_message.author.send(embed=reply)
        else:
            await d_message.channel.send(embed=reply)
    except mysql.connector.Error as error:
        print(f'Query error:{err}')
