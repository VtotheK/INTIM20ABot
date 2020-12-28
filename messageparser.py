import discord
import os 
import mysql.connector
import dbconnections as dbcon
import random


async def parse_message(message):
    msg = str(message.content).split(' ')
    map(str.lower, msg)
    print("here")
    if(msg[0] == '$bot'):
        if(len(msg) == 1):
            noargresponses = open("botresponses/emptyarg","r").readlines()
            response = noargresponses[random.randint(0,len(noargresponses)-1)]
            await message.channel.send(response)
            return
        if(message.content == "$bot hello"):
            response = "Hello there " + str(message.author.name) + "!"
            return
        if(message.content == "$bot -h"):
            emb = discord.Embed(title="Commands",color=0xc73228)
            emb.add_field(name="Help", value="$bot [-h|--help]", inline=False)
            emb.add_field(name="Leaderboard", value="$bot [-l|--leaderboard] [-dm||-directmessage]", inline=False)
            await message.channel.send(embed=emb)
            return
