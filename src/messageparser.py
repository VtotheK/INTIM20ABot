import discord
import os 
import mysql.connector
from db.connections import dbconnections as dbcon
import random
import leaderboard
import deadlinehandler

async def parse_message(d_message):
    msg = str(d_message.content).split(' ')
    map(str.lower, msg)

    if(msg[0] == '$bot'):
        if(len(msg) == 1):
            noargresponses = open('botresponses/emptyarg','r').readlines()
            response = noargresponses[random.randint(0,len(noargresponses)-1)]
            await d_message.channel.send(response)
            return
        if(d_message.content == '$bot hello'):
            response = 'Hello there ' + str(d_message.author.name) + '!'
            return
        if(msg[1] == '-h'):
            emb = discord.Embed(title='Commands',color=0xc73228)
            emb.add_field(name='Help', value='$bot [-h]', inline=False)
            emb.add_field(name='Leaderboard', value='$bot [-l] [-dm] [-p] <1-10>', inline=False)
            print(f'{d_message.author.id}')
            await d_message.channel.send(embed=emb)
            return
        if(msg[1] == '-l'):
            await leaderboard.call(d_message,msg)
        if(msg[1] == '-dl'):
            await deadlinehandler.parsemessage(d_msg,msg)

