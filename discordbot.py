#토큰을 위한 툴
from dotenv import load_dotenv
import os

#디스코드패키지
import discord

#로깅 툴
import logging
import logging.handlers

# #보안 툴
from auth import decrypt2


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

## 로깅

# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# discord.utils.setup_logging()
# discord.utils.setup_logging(level=logging.INFO, root=False)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes= 32 * 1024 * 1024, #32MB
    backupCount=5, #Rotate Through 5files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}][{levelname:<8}] {name}:{message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

## 디스코드 봇 토큰 가져오기
load_dotenv(stream=decrypt2())
TOKEN = os.getenv('DISCORD_TOKEN')

client.run(
    TOKEN, 
    log_handler=None, 
    # log_level=logging.DEBUG
    root_logger=True,
    )