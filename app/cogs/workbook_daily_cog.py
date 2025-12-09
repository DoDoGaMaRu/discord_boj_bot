import discord
from discord import app_commands
from discord.ext import commands
from db import SessionLocal

class WorkbookDailyCog(commands.Cog):
  def __init__(self, bot: commands.Bot):
      self.bot = bot

async def setup(bot: commands.Bot):
    await bot.add_cog(WorkbookDailyCog(bot))
