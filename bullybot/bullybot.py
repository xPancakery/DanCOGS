import discord
import lxml.html
import requests
import random
from redbot.core import commands
from .pcx_lib import type_message
from lxml import html

# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)

class bullybot(commands.Cog):
    #The premiere method of bullying your friends over discord. With a ROBOT. How absurd.

    @commands.command(aliases=["k"])
    async def bullyy(self, ctx: commands.Context):
        #Define the command for RedBot
        message = (await ctx.channel.history(limit=2).flatten())[1].content
        if not message:
            message = "Wait... I can't bully this!"
        else:
            await type_message(
            ctx.channel,
            self.bully_bot(message),
            allowed_mentions=discord.AllowedMentions(
                everyone=False, users=False, roles=False),
        )
        
    @staticmethod
    def bully_bot(message_input):
        # Set output and roll D20 for bully results
        output = []
        bully_skill = randint(1,20)
        
        if bully_skill == 1:
            pass
        elif bully_skill < 6: #Poopie
            # Reverse the words and shit on your friends with poop
            for word in message_input[::-1].split(' '):
                output.append(word[::-1].upper())
            return ':poop:'.join(output)
        elif bully_skill < 11: #Camel
            # Takes the previous message and returns it in cAmEl cAsInG.
            for let in range(len(message_input)):
                if let%2==0:
                    output.append(message_input[let].lower())
                else:
                    output.append(message_input[let].upper())
            return ''.join(output)
        elif bully_skill < 16: #Big boy words
            return insult_list
        elif bully_skill < 20:
            pass
        else:
            pass
    
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

def big_letters(self):
        # Embed the letters in code block for discord
        insult_out = ''
        insult_out += ('```py\n')
        # Print large format letters horizontally
        for i in range(len(letters['|'])):  
            for j in range(len(self)):       
                insult_out +=  letters[self[j]][i] + "   "#end = " ")
            insult_out += '\n'
        #finish the code block
        insult_out += ('```')
        return insult_out
    # Dictionary to call large format letters
def final(self):
        final_list = []
        for word in result.split(' '):
            if len(word) <= 12:
                final_list.append(word)
            else:
                pass
        return random.choice(final_list)

        # insult_list is the random insult big letter generator
insult_list = big_letters(final(final_list))
        
# Ideas for bully modules
# Replace spaces with the poop emojii and reverse word order in all caps (added for now)
# Return insult in 5x5 * letters (sold on this) [priority 1]
# Return toilet made out of characters (maybe??)
# Add .insult command with list of random insults called @user [priority 2]
# 
# 
# 
# 
