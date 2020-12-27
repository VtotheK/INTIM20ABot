import discord
import os 
import mysql.connector
import dbconnections as dbcon


async def parse_message(message):
    if(message.content == "$bot hello"):
        response = "Hello there " + str(message.author.name) + "!"
        await message.channel.send(response)
        try:
            conn = mysql.connector.connect(user=dbcon.user,password=dbcon.password,host=dbcon.host,database=dbcon.db)
            cur = conn.cursor()
            params = [message.author.id, message.author.name] 
            cur.callproc('')
            conn.commit()
            cur.close()
        except mysql.connector.Error as err:
            print(f"{err}")
        finally:
            conn.close()




