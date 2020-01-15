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
        print('hello')
        initial_date = date(date.today().year, 1, 1)
        percent = math.floor(date.today().day*100/366)
        year_bar = ''

        for i in range(5, 100, 5):
            year_bar = (i < percent) if year_bar + '▓' else year_bar + '░'

        embed = discord.Embed()
        embed.title = f'Progress Bar {date.today().year}'
        embed.description = f'<a:aSpriteCircle:605012000334151730> {year_bar} **{percent}%**'

        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(YearProgress(bot))
