import asyncio
import discord
from discord.ext import commands

class Upload(commands.Cog):

    def __init__(self, bot):
        self.bot = bot      

    @commands.command()
    @commands.guild_only()
    async def upload(self, ctx, link: str=None):
        message = ctx.message
        if link:
            await ctx.channel.send(link)
        elif len(message.attachments) > 1:
            await ctx.channel.send(message.attachments[0])
        else:
            await ctx.channel.send("Merci de renseigner une image à upload")

def setup(bot):
    bot.add_cog(Upload(bot))
