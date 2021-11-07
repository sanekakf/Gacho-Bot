import discord
from discord.ext import commands
import json
import os
import asyncio
from discord_components import DiscordComponents, Button, ButtonStyle

# Get configuration.json
with open("configuration.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]
	owner_id = data["owner_id"]


class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None
# Intents
intents = discord.Intents.all()
# The bot
bot = commands.Bot(prefix, intents = intents, owner_id = owner_id)
bot.remove_command("help")

# Load cogs
if __name__ == '__main__':
	for filename in os.listdir("Cogs"):
		if filename.endswith(".py"):
			bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")
	print(discord.__version__)
	DiscordComponents(bot)
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=".help"))
bot.run(token)
