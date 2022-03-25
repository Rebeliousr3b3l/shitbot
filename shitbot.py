import os
import discord
from dotenv import load_dotenv

#loading the bot's token
load_dotenv()
TOKEN = os.gentenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)