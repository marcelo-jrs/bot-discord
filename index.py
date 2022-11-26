import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant
import nltk

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

chatbot.load_model()

print("client running")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv('TOKEN')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$info"):
        response = chatbot.request(message.content[6:])
        await message.channel.send(response)

client.run(TOKEN)