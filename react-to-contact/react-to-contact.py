import re
import asyncio
import datetime
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class ReactToContact(commands.Cog):
    """
    Faire en sorte que les utilisateurs ouvre un ticket en cliquant sur un emoji
    """

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)
        self.reaction = None
        self.channel = None
        self.message = None
        # asyncio.create_task(self._set_db())

    # async def _set_db(self):
    #     config = await self.db.find_one({"_id": "config"})

    #     if config is None:
    #         return
    #     else:
    #         self.channel = config.get("channel", None)
    #         self.reaction = config.get("reaction", None)
    #         self.message = config.get("message", None)

    @commands.command(aliases=["sr"])
    @commands.guild_only()
    @checks.has_permissions(PermissionLevel.ADMIN)
    async def setreaction(self, ctx: commands.Context, link: str):
        """
        Définit le message sur lequel le bot va regarder les réactions.
        Crée une __session interactive__ via un emoji **(Prend également en charge les Emoji Unicode)**
        Avant d'utiliser cette commande, assurez-vous qu'il y a une réaction sur le message en question.

        **Usage:**
        {prefix}setreaction <message_url>
        """

        def check(reaction, user):
            return user == ctx.message.author

        regex = r"discordapp\.com"

        if bool(re.search(regex, link)) is True:
            sl = link.split("/")
            msg = sl[-1]
            channel = sl[-2]

            # TODO: Better English
            await ctx.send(
                "Réagir à ce message avec un emoji"
                " `(Cette réaction doit être ajoutée à ce message ou cela ne fonctionnera pas.)`"
            )
            reaction, user = await self.bot.wait_for("reaction_add", check=check)

            await self.db.find_one_and_update(
                {"_id": "config"},
                {
                    "$set": {
                        "channel": channel,
                        "message": msg,
                        "reaction": f"{reaction.emoji.name if isinstance(reaction.emoji, discord.Emoji) else reaction.emoji}",
                    }
                },
                upsert=True,
            )
            await ctx.send("Done!")

        else:
            await ctx.send("S'il vous plaît donner un lien de message valide")
            return

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.user_id == self.bot.user.id:
            return

        config = await self.db.find_one({"_id": "config"})

        if config is None:
          #  print("No Config")
            return

        if config["reaction"] is None or (payload.emoji.name != config["reaction"]):
          #  print("No Reaction")
            return

        if config["channel"] is None or (payload.channel_id != int(config["channel"])):
          #  print("No Channel")
            return

        if config["message"] is None or (payload.message_id != int(config["message"])):
          #  print("No Message")
            return

        guild: discord.Guild = discord.utils.find(
            lambda g: g.id == payload.guild_id, self.bot.guilds
        )

        member: discord.Member = guild.get_member(payload.user_id)

        channel = guild.get_channel(int(config["channel"]))

        msg: discord.Message = await channel.fetch_message(int(config["message"]))

        await msg.remove_reaction(payload.emoji, member)

        try:
            await member.send(
                embed=discord.Embed(
                    description="Bonjour, comment pouvons-nous vous aider ?", color=self.bot.main_color, footer="Attention répondre à ce message ouvrira un ticket support."
                )
            )
        except (discord.HTTPException, discord.Forbidden):
            ch = self.bot.get_channel(int(self.bot.config.get("575743860827750400")))

            await ch.send(
                embed=discord.Embed(
                    title="Le contact de l'utilisateur a échoué",
                    description=f"**{member.name}#{member.discriminator}** n'autorise pas les mp ou ma bloqué.",
                    color=self.bot.main_color,
                    timestamp=datetime.datetime.utcnow(),
                )
            )


def setup(bot):
    bot.add_cog(ReactToContact(bot))
