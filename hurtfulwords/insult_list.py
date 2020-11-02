import asyncio
import lxml
import requests
import lxml.html
import random

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
        
insult_out = big_letters(final(final_list))
        # insult_list is the random insult big letter generator
