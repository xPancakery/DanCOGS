import asyncio
import discord
import random
from redbot.core import commands
from .pcx_lib import type_message
from .insult_list import big_letters, final, final_list

class hurtfulwords(commands.Cog):
    #Insult your friends

    @commands.command(aliases=["i"])
    async def insult(self, ctx: commands.Context):
        #Define the command for RedBot
        message = (await ctx.channel.history(limit=2).flatten())[1].content
        if not message:
            message = "I big dumb dumb who can't think of insults"
        else:
            await type_message(
                ctx.channel,
                self.big_insults(),
                allowed_mentions=discord.AllowedMentions(
                    everyone=False, users=False, roles=False),
            )
            
    def big_insults(x):
        # Pick and print insult from insult_list
        return big_letters(final(final_list))
