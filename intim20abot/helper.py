import discord

def gethelpembed(command=None):
    leaderboard_value = '$bot -l [-dm] [-p] [-c <1-10>]'
    deadline_value = '$bot -dl [-dm] [-p] [c <1-999>]'

    if(command == None):
        emb = discord.Embed(title='**Commands**',color=0xc73228)
        info = '[] = Optional flags\n-dm = Direct message\n-p = Personal records\n-c = Limit search results'
        emb.add_field(name='**Help**', value='$bot -h [-dm]', inline=False)
        emb.add_field(name='**Leaderboard**', value=leaderboard_value, inline=False)
        emb.add_field(name='**Deadlines**', value=deadline_value,inline=False)
        emb.add_field(name='**Other**', value='$bot hello', inline=False)
        emb.add_field(name='**Other**', value='$bot', inline=False)
        emb.add_field(name='**General info**',value=info,inline=False)
        return emb
    elif(command == '-dl'):
        emb = discord.Embed(title='Arguments',color=0xc73228)
        emb.add_field(name=deadline_value, value=None,inline=False)
        emb.add_field(name='-c <1-999>', value='Limit the fetched rows to number defined after -c, Example: "$bot -dl -c 10" to get 10 deadlines.',inline=False)
        emb.add_field(name='-ld <1-30>', value='Get deadlines number of days from current time. Example: "$bot -dl -ld 7" to get deadlines which are due in 7 days or earlier.',inline=False)
        emb.add_field(name='-id <value>', value='Get deadline by DeadlineId.',inline=False)
        emb.add_field(name='-dm', value='Get deadlines as Direct Message (private message',inline=False)
        emb.add_field(name='-p', value='Only show your own personal deadlines.',inline=False)
        return emb
    elif(command == '-l'):
        emb = discord.Embed(title='Arguments',color=0xc73228)
        emb.add_field(name='-dm', value='Get leadboard as Direct Message (private message',inline=False)
        emb.add_field(name='-p', value='Only show your own personal postcount.',inline=False)
        emb.add_field(name='-c <1-10>', value='Limit the fetched rows to number defined after -c, Example: "$bot -l -c 5" to get top 5 posters.',inline=False)
        return emb
