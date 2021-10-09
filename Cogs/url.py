import discord
from discord.ext import commands


class Url(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "url",
                    usage="",
                    description = "Если вы потеряли ссылку на сайт, эта команда поможет")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def SendUrl(self, ctx:commands.Context):
        emb = discord.Embed(title="**http://gacho.herokuapp.com/main/**")
        await ctx.send(embed=emb)


def setup(bot:commands.Bot):
    bot.add_cog(Url(bot))