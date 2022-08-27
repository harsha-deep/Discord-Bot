import discord
from discord.ext import commands
from gif import get_gif
from meme import get_meme

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as', client.user)


@client.event
async def on_message(message):
    tokens = message.content.split(' ')

    if message.author == client.user:
        return

    if tokens[0] == 'gif':
        keywords_string = 'doge'  # by default
        if len(tokens) > 1:
            keywords = tokens[1:len(tokens)]
            keywords_string = ' '.join(keywords)
        [gif, desc] = get_gif(keywords_string)
        await message.channel.send(gif)
        await message.channel.send('GIF from Tenor: ' + desc)

    elif tokens[0] == 'reddit':
        subreddit = 'memes'  # by default
        [meme, author, title] = get_meme(tokens[1])
        await message.channel.send(meme)
        await message.channel.send(title)
        await message.channel.send('Meme posted in r/%s by u/%s' % (subreddit, author))
