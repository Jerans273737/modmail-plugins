from discord import Member
from discord.ext import commands
import asyncio

class InviteRecap(commands.Cog):
  
  async def __init__(self, bot):
    self.bot = bot
    self.joins = 0
    self.recap_channel = 698185668047667232

    while True:
        await self.bot.get_channel(recap_channel).send('test')
        await asyncio.sleep(10)

  @commands.Cog.listener()
  async def on_member_join(self, member):
    self.joins = self.joins + 1

def setup(bot):
  bot.add_cog(InviteRecap(bot))
