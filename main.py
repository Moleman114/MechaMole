# This is an experimental discord bot for testing purposes
# This file is the main portion of the bot and will use other files
# Author: Jett Bolen (AKA Moleman)
# Date: 2023-05-10 7:55 PM


import discord
import logging
import requests
import json


# discord API setup
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# logging setup
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


# -- CONSTANTS --
# These are the parameters of the bot (i.e. it's settings, only editable in code)
with open('mechamole_priv_token.txt') as f:
    token = f.readlines()[0]

# -- STATIC VARIABLES --
prefix = 'm.'

# -- HELPER METHODS --
# These are methods that will be called by bot events to assist

# get_quote will get a random quote from the zenquotes API
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

# -- BOT EVENTS --
# These are the bots events (what it will do when it encounters something)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    # if the message was written by the bot, ignore
    if message.author == client.user:
        return

    if message.content.startswith(f'{prefix}hello'):
        await message.channel.send('Hello!')

    if message.content.startswith(f'{prefix}inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    # in pogress
    """if message.content.contains('fuck'):
        await message.delete()
        message_author = await message.author
        await message.channel.send(f'Sorry {message_author.user}, no swearing!')"""


# MAKE SURE NOT TO SHOW THIS TOKEN TO ANYONE
client.run(token, log_handler=handler)
