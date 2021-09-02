import os
import discord
import requests
import json
import random
from keep alive_alive import keep_alive

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing", "sourpuss", "scared"]

starter_encourgements = ["Cheer up buddy", "Hang in there man", "You are a great person / bot!", "You are not alone", "You are amazing"]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user} '.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content

    if message.content.startswith('$Hi Bot'):
        await message.channel.send('Hello')

    if message.content.startswith('$inspire me'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice (starter_encourgements))

client.run('ODc4Mzk1NDM1NDQ4OTUwODI0.YSAjfw.idIeILqf29HBIThVWIOzbDHI0dw')
