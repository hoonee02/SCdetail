#토큰을 위한 툴
from dotenv import load_dotenv
import os

#디스코드패키지
import discord



class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

## 디스코드 봇 토큰 가져오기
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client.run(TOKEN)