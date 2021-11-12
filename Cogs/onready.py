import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
import asyncio

class sdi(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        async def sended():
            guild = self.bot.get_guild(878549296709001267)
            channel = guild.get_channel(904735863215366204)
            await channel.purge()
            embed=discord.Embed(title="Выбери себе роль ниже!", description="**`Заметь!`**, что можно выбрать только 1 роль и сменить её уже нельзя будет!", color=0xff0000)
            embed.set_author(name="G-Inc", url="http://gacho.herokuapp.com/main/", icon_url="https://cdn.discordapp.com/attachments/903735310339420260/904728141606584360/Halloween_Logo.png")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/861649193722839050/904813585664970833/103230.png")
            heart=self.bot.get_emoji(904811750766030918)
            dung=self.bot.get_emoji(904825175864922202)
            floppa=self.bot.get_emoji(904822289529442354)
            await channel.send(
                embed=embed,
                components = [
                    Select(
                        placeholder = "Выбери роль тут!",
                        options = [
                            SelectOption(label = "BIG FLOPPA", value = "896831403902259210", emoji=floppa),
                            SelectOption(label = "DUNGEON MASTER", value = "878574107577425921", emoji=dung),
                            SelectOption(label="VAN", value="904825530778542091", emoji=heart)
                        ]
                    )
                ]
            )
            while True:
                interaction = await self.bot.wait_for("select_option")
                opinion= int(interaction.values[0])
                guild = self.bot.get_guild(878549296709001267)
                selected = guild.get_role(opinion)
                remove = guild.get_role(904735144877899866)
                author = interaction.author
                if selected.name.lower() == 'dungeon master':
                    embed=discord.Embed(title="!ОТСОРОЖНО!", description="Выбор роли ***DUNGEON MASTER***, Обязует адекватное обращение, ибо лишь истинные люди могут иметь роль DM. __Грозит баном__", color=0x000000)
                    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/564/564619.png")
                    components = [
                        [
                            Button(emoji = self.bot.get_emoji(904811443998834709) , style=ButtonStyle.green, custom_id='agree'),
                            Button(emoji = self.bot.get_emoji(904811420183564372) , style=ButtonStyle.red, custom_id='disagree')
                        ]
                    ]
                    msg = await interaction.send(
                        embed=embed,
                        components = components
                    )
                    components
                    while True:
                        try:
                            interaction = await self.bot.wait_for(
                                'button_click',
                                check=lambda inter: inter.message.id == msg.id,
                                timeout=60
                            )

                        except asyncio.TimeoutError:
                            for row in components:
                                row.disable_components()
                            return await msg.edit(content='Время вышло', components=components)
                        opt = interaction.custom_id
                        if opt == "agree":
                            await author.remove_roles(remove)
                            await author.add_roles(selected)
                            channel = guild.get_channel(878573211745402910)
                            embed=discord.Embed(title="ВНИМАНИЕ", description="На нашем сервере появился новый *__Dungeon Master__*", color=0xfff000)
                            embed.add_field(name="Будьте осторжны и бдительны", value=f"Поскольку {interaction.author} выбрал такую важную роль. Он должен проявить максимальную адекватность! И соответственно получить достойное уважение", inline=False)
                            await channel.send(embed=embed)
                        elif opt == 'disagree':
                            await sended()

                else:
                    await author.add_roles(selected)
                    await author.remove_roles(remove)
                msg = await interaction.send(content = f"{selected.name} выбран!")
                await channel.purge()
                await sended()



        guild = self.bot.get_guild(878549296709001267)
        channel = guild.get_channel(904735863215366204)
        await channel.purge()
        await sended()
        
def setup(bot:commands.Bot):
    bot.add_cog(sdi(bot))