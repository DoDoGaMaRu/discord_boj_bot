import discord
from sqlalchemy import exists, update, and_

from db import SessionLocal
from discord import app_commands
from discord.ext import commands
from models import Guild, Member
from logger import logger

# TODO: name, description 조정
class GuildCog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_guild_join(self, guild: discord.Guild):
    logger.info(guild.name + " joined")
    await self.find_guild(guild)

  @app_commands.command(name="join", description="문제 배달 받기")
  async def _join(self, interaction: discord.Interaction):
    guild = await self.find_guild(interaction.guild)
    await self.join_guild(interaction.user, guild)
    await interaction.response.send_message("문제 배달이 등록되었어요", ephemeral=True)

  @app_commands.command(name="leave", description="문제 배달 그만받기")
  async def _leave(self, interaction: discord.Interaction):
    guild = await self.find_guild(interaction.guild)
    await self.leave_guild(interaction.user, guild)
    await interaction.response.send_message("이제부터 문제 배달을 받지 않아요", ephemeral=True)

  @app_commands.command(name="members", description="문제 배달을 받는 사람들")
  async def _members(self, interaction: discord.Interaction):
    guild = await self.find_guild(interaction.guild)

    session = SessionLocal()
    members = session.query(Member).filter(
      (Member.guild_id == guild.id) &
      (Member.is_activated == True)
    ).all()

    # TODO: 문제 받는 사람 목록 표시
    await interaction.response.send_message(len(members), ephemeral=True)

  async def find_guild(self, _guild: discord.Guild):
    session = SessionLocal()
    guild = session.query(Guild).filter(Guild.guild_id == _guild.id).first()

    if guild is None:
      guild = Guild(guild_id=_guild.id)
      session.add(guild)
      session.commit()
      logger.info(f"서버 등록: {guild.id}")
    return guild

  async def join_guild(self, user: discord.User, guild: Guild):
    session = SessionLocal()
    member = session.query(Member).filter(
      (Member.guild_id == guild.id) &
      (Member.discord_id == user.id)
    ).first()

    if member is None:
      member = Member(guild_id=guild.id, discord_id=user.id, is_activated=True)
      session.add(member)
      logger.info(f"사용자 등록: {member.id}")
    else:
      stmt = update(Member).where(
        (Member.guild_id == guild.id) &
        (Member.discord_id == user.id)
      ).values(is_activated=True)
      session.execute(stmt)
    session.commit()

  async def leave_guild(self, user: discord.User, guild: Guild):
    session = SessionLocal()

    stmt = update(Member).where(
      (Member.guild_id == guild.id) &
      (Member.discord_id == user.id)
    ).values(is_activated=False)
    session.execute(stmt)
    session.commit()

async def setup(bot: commands.Bot):
    await bot.add_cog(GuildCog(bot))
