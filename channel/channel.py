import asyncio, discord
from   discord.ext import commands
from   discord     import Forbidden

class Channel(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    channelAttachments = int
    
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMIN)
    async def media(self, ctx: commands.Context, mediaid: int):
        channelAttachments = mediaid
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == channelAttachments:
            await message.channel.send(len(message.content))

def setup(bot):
    bot.add_cog(Channel(bot))
