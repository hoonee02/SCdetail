import discord
class myClient(discord.Client):
    async def on_ready(self):
        print(f'logged on as {self.user}!')
    
    async def on_message(self,message):
        print(f'Message form {message.author}: {message.coontent}')

intents = discord.Intents.default()
intents.message_content = True

client = myClient(intents=intents)
client.run('c7494e25b8b8def03d1a8c59c0d13d5528636073ec92054e6349840769f5d7a2')