import discord

intents = discrod.intents.default()
intents.message_content = True

client = discrod.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client
async def on_message(message):
    if message.author == client.user:
        return
    
    if meassage.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run("c7494e25b8b8def03d1a8c59c0d13d5528636073ec92054e6349840769f5d7a2")