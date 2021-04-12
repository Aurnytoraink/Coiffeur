import json
from pathlib import Path
import discord

##############

# PATH = Path("/home/aurnytoraink/Bot/Coiffeur")
PATH = Path("/home/aurnytoraink/Projets/Code/Bot/Coiffeur")

TOKEN = json.loads(open(PATH/"config.json",'rb').read())["token"]

#############
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('quoi'):
        await message.channel.send("FEUR!!!!")

client.run(TOKEN)