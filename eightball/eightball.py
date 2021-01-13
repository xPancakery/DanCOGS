import random
import discord
from .pcx_lib import type_message
from redbot.core import commands


class magic_ball(commands.Cog):

    @commands.command(aliases=["8ball"])
    async def magic_ball(self, ctx: commands.Context, question):
        message = (await ctx.channel.history(limit=2).flatten())
        if not message:
            message = "You must ask a question to the Magic 8 Ball."
        else:
            await type_message(
                ctx.channel,
                self.qna(question),
                allowed_mentions=discord.AllowedMentions(
                    everyone=False, users=False, roles=False),
            )
        

    def qna(self, question):
        answer = ''
        choices = ['As I see it, yes.','Ask again later.','Better not tell you now.','Cannot predict now.','Concentrate and ask again.',
        "Don't count on it.",'It is certain.','It is decidedly so.','Most likely','My reply is no.',
        'My sources say no.','Outlook not so good.','Outlook good.','Reply hazy, try again.','Signs point to yes.',
        'Very doubtful','Without a doubt.','Yes.','Yes - definitely.','You may rely on it.']
        if '?' in question[-1:]:
            answer = random.choice(choices)
            return(answer)
        else:
            return("Ask a question to the Magic 8 Ball.")
        
