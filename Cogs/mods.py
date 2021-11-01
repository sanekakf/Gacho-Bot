import discord
from discord.ext import commands


class Moderators(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "clear",
                    usage="<Количество>",
                    description = "Удаляет выбранное вам количество сообщений")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def clear(self, ctx:commands.Context, number:int):
        if number:
            try:
                msgs = await ctx.channel.purge(limit=number)
                await ctx.send(f"Успешно ")
            except Exception:
                await ctx.send("Ошибка")


def setup(bot:commands.Bot):
    bot.add_cog(Moderators(bot))