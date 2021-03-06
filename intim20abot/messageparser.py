import discord
import helper
import os 
import mysql.connector
import random
import leaderboard
import deadlinehandler
from db.connections import dbconnections as dbcon

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
            await d_message.channel.send(response)
            return
        if(msg[1] == '-h'):
            cmd = None
            if(len(msg) >= 2):
                pass
            emb = helper.gethelpembed(command=cmd)
            if('-dm' in msg):
                await d_message.author.send(embed=emb)
            else:
                await d_message.channel.send(embed=emb)
        if(msg[1] == '-l'):
            await leaderboard.sendleaderboard(d_message,msg)
            return
        if(msg[1] == '-dl'):
            await deadlinehandler.parsemessage(d_message,msg)
            return
        #if(msg[1] == '-t'):
        #    await d_message.channel.send(file=discord.File(r'template.txt'))
        else:
            await d_message.channel.send("I dont know what you want, type -h for available commands")

