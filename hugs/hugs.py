from discord import Member
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def hug(self, ctx, member: Member): 
        await ctx.send(f":information_source: {member.mention} tu a reçu un gros calin de la part de {ctx.author.mention} <a:awumpusheart:622779992258117674>")
        await ctx.message.delete()
  
        
    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await msg.channel.send(f"Désolé {ctx.author.mention}, mais je n'ai pas trouvé d'utilisateur à hug :(")
        elif isinstance(error, commands.BadArgument):
            await msg.channel.send(f"Désolé {ctx.author.mention}, mais il faut que tu mentionne ou que tu donne l'id de l'utilisateur à hug")
    
    def setup(bot):
        bot.add_cog(MyCog(bot))
