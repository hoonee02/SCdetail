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

client.run("MTE4OTQ2MTYyNjk3NDM4NDIwOQ.GfqVXW.-B5ysOsMy8-gNTDyz_DRPzOqMqfUdc8d5RG0nE")