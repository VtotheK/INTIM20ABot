import discord

def gethelpembed(command=None):
    if(command == None):
        emb = discord.Embed(title='**Commands**',color=0xc73228)
        info =  '[] = Optional flags\n-dm = Direct message\n-p = Personal records\n-c = Limit search results'
        emb.add_field(name='**Help**', value='$bot -h [-dm]', inline=False)
        emb.add_field(name='**Leaderboard**', value='$bot -l [-dm] [-p] [-c <1-10>]', inline=False)
        emb.add_field(name='**Deadlines**', value='$bot -dl [-dm] [-p] [c <1-999>]',inline=False)
        emb.add_field(name='**Other**', value='$bot hello', inline=False)
        emb.add_field(name='**Other**', value='$bot', inline=False)
        emb.add_field(name='**General info**',value=info,inline=False)
        return emb
