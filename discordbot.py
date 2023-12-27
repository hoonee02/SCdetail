#토큰을 위한 툴
from dotenv import load_dotenv
import os

#디스코드패키지
import discord

#로깅 툴
import logging
import logging.handlers

#보안 툴
import binascii
import urllib.parse
import requests
from io import StringIO


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

## 관계자 외 출입금지
def decrypt(string):
    # 16진수를 ASCII로 디코딩
    decoded = binascii.unhexlify(string.encode()).decode()

    # ASCII를 URL 형식으로 디코딩
    decoded_fi = urllib.parse.unquote(decoded)
    return decoded_fi
url = '68747470732533412f2f63646e2e646973636f72646170702e636f6d2f6174746163686d656e74732f313138393535383433363533353438303332302f313138393535383632393233303138323530302f656e762533466578253344363539653939636525323669732533443635386332346365253236686d25334432633036333662643766323334326530383162363839386566616436346535353838353362373135343231313361346162633663633462633835383238636238253236'
decrypted_url = decrypt(url)
response = requests.get(decrypted_url)
confidential_content = response.text
confidential_obj = StringIO(confidential_content)


## 디스코드 봇 토큰 가져오기
load_dotenv(stream=confidential_obj)
TOKEN = os.getenv('DISCORD_TOKEN')

client.run(
    TOKEN, 
    log_handler=None, 
    # log_level=logging.DEBUG
    root_logger=True,
    )