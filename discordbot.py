import discord
class myClient(discord.Client):
    async def on_ready(self):
        print(f'logged on as {self.user}!')
    
    async def on_message(self,message):
        print(f'Message form {message.author}: {message.coontent}')

intents = discord.Intents.default()
intents.message_content = True

client = myClient(intents=intents)
client.run('MTE4OTQ2MTYyNjk3NDM4NDIwOQ.GfqVXW.-B5ysOsMy8-gNTDyz_DRPzOqMqfUdc8d5RG0nE')