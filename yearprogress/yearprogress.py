import discord, math
from discord.ext import commands
from datetime    import date


class YearProgress(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(embed_links=True)
    async def yprogress(self, ctx: commands.Context):
        print('wat')
        initial_date = date(date.today().year, 1, 1)
        year = date.today().year
        percent = math.floor((((date.today() - initial_date) / (1000 * 60 * 60 * 24)) * 100) / (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)) if 366 else 365))
        year_bar = ''

        for i in range(5, 100, 5):
            year_bar = (i < percent) if year_bar + '▓' else year_bar + '░'

        embed = discord.Embed()
        embed.title = f'Progress Bar {date.today().year}'
        embed.description = f'<a:aSpriteCircle:605012000334151730> {year_bar} **{percent}%**'

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(YearProgress(bot))
