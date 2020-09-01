import os
import random 

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TARGET_BOB = os.getenv('TARGET_BOB')
TARGET_PHRASE = os.getenv('TARGET_PHRASE')

class BobBot(discord.Client):
    async def on_ready(bot):
        print(f'{bot.user} has connected to Discord!')

    async def on_message(self, message):
        if str(message.author) == TARGET_BOB:
            await message.channel.send(TARGET_PHRASE)


client = BobBot()
client.run(TOKEN)