import asyncio
import discord
from discord.ext import commands

class Upload(commands.Cog):

    def __init__(self, bot):
        self.bot = bot      

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def upload(self, ctx):
        ctx.send("test")
         

def setup(bot):
    bot.add_cog(Upload(bot))
