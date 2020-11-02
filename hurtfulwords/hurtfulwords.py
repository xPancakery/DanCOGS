import discord
from redbot.core import commands
from .pcx_lib import type_message
import lxml.html
import lxml
import random
import requests

class hurtfulwords(commands.Cog):
    #Insult your friends

    @commands.command(aliases=["i"])
    async def hwords(self, ctx: commands.Context):
        #Define the command for RedBot
        message = (await ctx.channel.history(limit=2).flatten())[1].content
        if not message:
            message = "I can't translate that!"
        await type_message(
            ctx.channel,
            self.big_insults(message),
            allowed_mentions=discord.AllowedMentions(
                everyone=False, users=False, roles=False),
        )
        
    @staticmethod
    def big_insults(x):
        return insult_list

    letters = {         
    'a':['  *  ',' * * ','*****','*   *','*   *'],
    'b':['**** ','*   *','*****','*   *','**** '],
    'c':[' ****','*    ','*    ','*    ',' ****'],
    'd':['**** ','*   *','*   *','*   *','**** '],
    'e':['*****','*    ','*****','*    ','*****'],
    'f':['*****','*    ','*****','*    ','*    '],
    'g':['*****','*    ','* ***','*   *','*****'],
    'h':['*   *','*   *','*****','*   *','*   *'],
    'i':['*****','  *  ','  *  ','  *  ','*****'],
    'j':['***  ','  *  ','  *  ','  *  ','***  '],
    'k':['*   *','* *  ','*    ','* *  ','*   *'],
    'l':['*    ','*    ','*    ','*    ','*****'],
    'm':['*   *','** **','* * *','*   *','*   *'],
    'n':['*   *','**  *','* * *','*  **','*   *'],
    'o':[' *** ','*   *','*   *','*   *',' *** '],
    'p':['**** ','*   *','**** ','*    ','*    '],
    'q':[' *** ','*   *','* * *','*  * ',' ** *'],
    'r':['**** ','*   *','**** ','* *  ','*  **'],
    's':[' ****','*    ',' *** ','    *','**** '],
    't':['*****','  *  ','  *  ','  *  ','  *  '],
    'u':['*   *','*   *','*   *','*   *',' *** '],
    'v':['*   *','*   *',' * * ',' * * ','  *  '],
    'w':['*   *','*   *','* * *','* * *',' * * '],
    'x':['*   *',' * * ','  *  ',' * * ','*   *'],
    'y':['*   *',' * * ','  *  ','  *  ','  *  '],
    'z':['*****','   * ','  *  ',' *   ','*****'],
    ',':['     ','     ','   **','   **','  *  '],
    ':':['     ','  *  ','     ','  *  ','     '],
    '|':['*****','*****','*****','*****','*****'],
    ' ':['','','','','']
    }

    html = requests.get('http://www.insult.wiki/list-of-insults')
    doc = lxml.html.fromstring(html.content)
    insults_list = doc.xpath('//html/body/ol/li/a/@href')
    insult_string = ''.join(insults_list)
    remove_html = 'http://www.insult.wiki/insult/'
    result = insult_string.replace(remove_html,' ')
    final_list = []
        # Large letter command

    def big_letters(insult):
        # Embed the letters in code block for discord
        insult_out = ''
        insult_out += ('```py\n')
        # Print large format letters horizontally
        for i in range(len(letters['|'])):  
            for j in range(len(insult)):       
                insult_out +=  letters[insult[j]][i] + "   "#end = " ")
            insult_out += '\n'
        #finish the code block
        insult_out += ('```')
        return insult_out
        # Dictionary to call large format letters
    def final(x):
        final_list = []
        for word in result.split(' '):
            if len(word) <= 12:
                final_list.append(word)
            else:
                pass
        return random.choice(final_list)

        # insult_list is the random insult big letter generator
    insult_list = big_letters(final(final_list))
