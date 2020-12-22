import discord


async def parse_message(message):
    if(message.content == "$bot hello"):
        response = "Hello there " + str(message.author.name) + "!"
        await message.channel.send(response)
