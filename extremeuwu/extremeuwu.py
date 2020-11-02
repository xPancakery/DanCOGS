import discord
import random
from redbot.core import commands
from .pcx_lib import type_message

class extremeuwu(commands.Cog):
    #The newer crazier UwU command

    @commands.command(aliases=["xuwu"])
    async def extremeuwu(self, ctx: commands.Context):
        #Define the command for RedBot
        message = (await ctx.channel.history(limit=2).flatten())[1].content
        if not message:
            message = "***OMAE WA MOU SHINDEIRU***"
        else:
            await type_message(
            ctx.channel,
            self.exuwu(message),
            allowed_mentions=discord.AllowedMentions(
                everyone=False, users=False, roles=False),
        )
        
    @staticmethod
    def exuwu(message_input):
        output = ''
        vowels = '[a,e,i,o,u]'
        for letter in message_input.lower():
            if letter not in vowels:
                output += letter
            elif letter in vowels:
                if letter == 'a':
                    output += 'awa'
                elif letter == 'e':
                    output += 'ewe'
                elif letter == 'i':
                    output += 'iwi'
                elif letter == 'o':
                    output += 'owo'
                elif letter == 'u':
                    output += 'uwu'
                elif letter == 'y':
                    output += 'ywy'
        return output
