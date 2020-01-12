import discord, math
from   discord.ext import commands
from   datetime    import date


class YProgress(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_leap_year(year): 
        return (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0))

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def yprogress(self):
        initial_date = date(date.today().year, 1, 1)
        year = date.today().year
        percent = math.floor((((date - initial_date) / (1000 * 60 * 60 * 24)) * 100) / (is_leap_year(date.today().year) if 366 else 365))
        year_bar = ''

        for range(5, 100, 5):
            year_bar = (i < percent) if year_bar + '▓' else year_bar + '░'

        embed = discord.Embed()
        embed.title = f'Progress Bar {date.today().year}'
        embed.description = f'<a:aSpriteCircle:605012000334151730> {year_bar} **{percent}%**'

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(YProgress(bot))
