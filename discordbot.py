import discord
class myClient(discord.Client):
    async def on_ready(self):
        print(f'logged on as {self.user}!')
    
    async def on_message(self,message):
        print(f'Message form {message.author}: {message.coontent}')

intents = discrod.intents.default()
intents.message_content = Ture

client = Myclient(intents=intents)
client.run('my token goes here')