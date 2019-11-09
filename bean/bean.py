import asyncio, discord
from   discord.ext import commands
from   discord     import Forbidden

class Bean(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def bean(self, ctx, target: discord.Member):
        beanEmoji = ctx.bot.get_emoji(642785892603265024)

        await ctx.send('<:bean:{}> Beaned **{}** (`{}`)!'.format(beanEmoji.id, ctx.author, ctx.author.id))
        try:
            message = await self.bot.wait_for('message', timeout=60*5, check=lambda m: m.author == target and m.channel.guild == ctx.guild)
        except asyncio.TimeoutError:
            pass
        else:
            try:
                await message.add_reaction(beanEmoji)
            except Forbidden:
                await message.channel.send('<:bean:{}>'.format(beanEmoji.id))

def setup(bot):
    bot.add_cog(Bean(bot))