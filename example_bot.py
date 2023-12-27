#토큰을 위한 툴
from dotenv import load_dotenv
import os

#디스코드패키지
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client
async def on_message(message):
    if message.author == client.user:
        return
    
    if meassage.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run( )