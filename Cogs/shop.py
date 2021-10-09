import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class Shop(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "shop",
                    usage="",
                    description = "Показывает товары с магазина")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def fetch(self, ctx:commands.Context):
        response = requests.get('http://gacho.herokuapp.com/pricing/')
        soup = BeautifulSoup(response.text, 'lxml')
        products = soup.find_all('div', class_='col')
        emb = discord.Embed(title="G-Shop", color=0xffa161, url='http://gacho.herokuapp.com/pricing/')

        for i in range(0, len(products)):
            name = products[i].find_all('h4')
            feature = products[i].find_all('ul')
            price = products[i].find_all('h1')
            emb.add_field(name=name[0].text, value=f'Заметка: {feature[0].text}\nЦена: {price[0].text}', inline=False)

        emb.set_footer(text="Gacho-Inc.", icon_url="https://cdn.discordapp.com/attachments/888720944166740028/896431088312913920/Gacho-Ico.png")
        await ctx.send(embed=emb)

        


def setup(bot:commands.Bot):
    bot.add_cog(Shop(bot))