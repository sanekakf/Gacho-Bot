import discord
from discord.ext import commands
import psycopg2

conn = psycopg2.connect(dbname='d8oesgokub4tbi', user='skymohsmnwiqsv', 
                        password='2ff98136707ba1ee29690a750d0c77052a29939117be706e036ec5d6236ef867', host='ec2-52-210-120-210.eu-west-1.compute.amazonaws.com')
cur = conn.cursor()

class JoinLeave(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        roleId = 904735144877899866
        # cur.execute(f"SELECT * FROM slaves WHERE id = %s", (member,))
        # res = cur.fetchall()
        me= self.bot.fetch_user(447030106179764226)
        print(member._user)
        # if res:
            # await member.add_roles(roleId, reason="Приветствие нового Slave!")
        # else:
            # cur.execute("INSERT INTO slaves VALUES(%s)", (member._user,))
            # await member.add_roles(roleId, reason="Приветствие нового Slave!")
        await me.send(f"Новый участник {member}!")

    # @commands.command(name = "send", description="Временная команда")
    # async def  commandName(self, ctx:commands.Context):
    #     embed=discord.Embed(title="Добро пожаловать, Boy next door!", color=0x83cdfb)
    #     embed.set_author(name="G-Inc", url="http://gacho.herokuapp.com/main/", icon_url="https://cdn.discordapp.com/attachments/903735310339420260/904728141606584360/Halloween_Logo.png")
    #     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/878568713564094464/904731358503530537/Billy.png")
    #     embed.add_field(name="MINI-ВЕРИФИКАЦИЯ", value="Выберите себе нужную роль в -> <#904735863215366204> и получи доступ к основным каналам", inline=True)
    #     embed.set_footer(text="lets celebrate...")
    #     await ctx.send(embed=embed)

    # @commands.Cog.listener()
    # async def on_member_remove(self, member:discord.Member):



def setup(bot:commands.Bot):
    bot.add_cog(JoinLeave(bot))