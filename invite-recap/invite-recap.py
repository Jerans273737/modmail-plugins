from discord import Member
from discord.ext import commands
import asyncio

class MyCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.joins = 0
    self.recap_channel = 698185668047667232

  async def recap(self):
    while True:
        await self.bot.get_channel(recap_channel).send(f'> **{joins}** nouveaux membres')
        self.joins = 0
        await asyncio.sleep(300)

  @commands.Cog.listener()
  async def on_member_join(self, member):
    self.bot.loop.create_task(self.recap())
    self.joins = self.joins + 1

def setup(bot):
  bot.add_cog(MyCog(bot))
