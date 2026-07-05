"""
🚽 Skibiditopia Brainrot Notifier — ULTRA QLOW v7"""
import discord, asyncio, random, os
from datetime import datetime, timezone
from dotenv import load_doten
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
FOOTER = ".GG/skibiditopia"
TITLE = "🚽 SKIBIDITOPIA FOUND"
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True
bot = discord.Client(intents=intents)
URLS = {
    "Garama and Madundung": "https://static.wikia.nocookie.net/stealabr/images/e/ee/Garamadundung.png/revision/latest?cb=20250816022557",
}
print("FIXED")