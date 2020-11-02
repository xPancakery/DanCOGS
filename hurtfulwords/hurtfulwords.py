import discord
from redbot.core import commands
from .pcx_lib import type_message
from .insult_list import insult_out

class hurtfulwords(commands.Cog):
    #Insult your friends

    @commands.command(aliases=["i"])
    async def insult(self, ctx: commands.Context):
        #Define the command for RedBot
        message = (await ctx.channel.history(limit=2).flatten())[1].content
        if not message:
            message = "I'm a dumb boy who can't think of insults"
        await type_message(
            ctx.channel,
            self.big_insults,
            allowed_mentions=discord.AllowedMentions(
                everyone=False, users=False, roles=False),
        )
        
    
    def big_insults(self):
        return insult_out
