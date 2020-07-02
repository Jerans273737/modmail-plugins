import discord, math
from discord.ext import commands
import datetime as dt


class YearProgress(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['yearprogress', 'progress', 'year'])
    @commands.guild_only()
    @commands.has_permissions(embed_links=True)
    async def yprogress(self, ctx: commands.Context):
        today = dt.date.today()
        next_year = dt.date(dt.date.today().year + 1, 1, 1)
        progress = (next_year - today).days / 365 * 100
        year_bar = ''

        for i in range(5, 100, 5):
            if i < progress:
                year_bar = year_bar + '▓' 
            else:
                year_bar = year_bar + '░'

        embed = discord.Embed()
        embed.colour = discord.Colour(0x36393f)
        embed.title = f'Progress Bar {dt.date.today().year}'
        embed.description = f'<a:aSpriteCircle:605012000334151730> {year_bar} **{progress:.2f}%**'

        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(YearProgress(bot))
