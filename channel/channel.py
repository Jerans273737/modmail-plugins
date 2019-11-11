import asyncio, discord
from   discord.ext import commands
from   discord     import Forbidden

class Channel(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.channelAttachments = int
    
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMIN)
    async def media(self, ctx: commands.Context, mediaid: int):
        self.channelAttachments = bot.get_channel(mediaid)
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == self.channelAttachments.id:
            await message.channel.send(message.content)

def setup(bot):
    bot.add_cog(Channel(bot))
