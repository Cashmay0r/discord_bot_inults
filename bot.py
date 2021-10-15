# bot.py
from operator import length_hint
import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

f = open('classic.txt')
insults = []
serverUsers = {}
for insult in f:
    insults.append(insult)
    
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
        if guild.name == GUILD:
            break
        for member in guild.members:
            serverUsers[member.name] = member.id
        print(serverUsers)
        


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'pog':
        randomNum = random.randint(0, len(insults))
        await message.channel.send(insults[randomNum])
        for user in serverUsers:
           
            userID = (f"<@{str(serverUsers[user])}>")
            msg = user + '=' + str(serverUsers[user])
            await message.channel.send(userID)
     
    
client.run(TOKEN)
