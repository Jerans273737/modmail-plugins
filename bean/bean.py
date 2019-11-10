import asyncio, discord
from   discord.ext import commands
from   discord     import Forbidden

class Bean(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.beanEmoji = bot.get_emoji(642785892603265024)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def bean(self, ctx, target: discord.Member, flags: str=None):
        if flags != "-s":
            await ctx.send('<:ItemBean:{}> Beaned **{}** (`{}`)'.format(self.beanEmoji.id, target, target.id))
        else:
            await ctx.message.delete()

        try:
            message = await self.bot.wait_for('message', timeout=60*5, check=lambda m: m.author == target and m.channel.guild == ctx.guild)
        except asyncio.TimeoutError:
            pass
        else:
            try:
                await message.add_reaction(self.beanEmoji)
            except Forbidden:
                await message.channel.send('<:ItemBean:{}>'.format(self.beanEmoji.id))

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.count >= 5 and reaction.emoji.id == self.beanEmoji.id:
            wowee = await reaction.message.channel.send('WOWEEEEE SUPER BEAAN <:ItemBean:{}>'.format(self.beanEmoji.id))
            await wowee.add_reaction(self.beanEmoji)

def setup(bot):
    bot.add_cog(Bean(bot))