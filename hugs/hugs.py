from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        args = msg.content.split(" ")
        if args[0].startswith("!"):
            if args[0].replace("!", "") == "hug":
                if len(args) > 1:
                    if len(msg.mentions) > 0:
                        for user in msg.mentions:
                            fuser = user
                    else:
                        try:
                            fuser = bot.get_user(args[1])
                        except:
                            await msg.channel.send(f"Désolé {msg.author.mention}, mais je n'ai pas trouvé d'utilisateur à hug :(")
                            return
                    await msg.channel.send(f":information_source: {fuser.mention} tu a reçu un gros calin de la part de {msg.author.mention} <a:awumpusheart:622779992258117674>")
                    await msg.delete()
                else:
                    await msg.channel.send(f"Désolé {msg.author.mention}, mais il faut que tu mentionne ou que tu donne l'id de l'utilisateur à hug")


    def setup(bot):
        bot.add_cog(MyCog(bot))
