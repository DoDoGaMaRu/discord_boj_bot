import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
DEBUG = os.getenv("DEBUG") == "True"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

from logger import logger

# ----------------------
# INITIALIZE
# ----------------------
@bot.event
async def on_ready():
  logger.info(f'{bot.user} 로그인 성공')

  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      await bot.load_extension(f'cogs.{filename[:-3]}')

  await bot.change_presence(status=discord.Status.online, activity=discord.Game('문제 고르는 중'))
  try:
    synced = await bot.tree.sync()
    logger.info(f"Slash commands synced: {len(synced)}")
  except Exception as e:
    logger.error(e)

# ----------------------
# run
# ----------------------
bot.run(TOKEN)