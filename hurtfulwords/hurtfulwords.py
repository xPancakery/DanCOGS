import asyncio
import discord
from redbot.core import commands
from .pcx_lib import type_message
from .insult_list import insult_out

class hurtfulwords(commands.Cog):
    #Insult your friends

    @commands.command(aliases=["i"])
    async def insult(self, ctx: commands.Context):
        #Define the command for RedBot
        return insult_out
