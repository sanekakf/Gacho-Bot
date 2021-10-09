import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, NotOwner
import time


class OnCommandErrorCog(commands.Cog, name="on command error"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_command_error(self, ctx:commands.Context, error:commands.CommandError):
		if isinstance(error, commands.CommandOnCooldown):
			day = round(error.retry_after/86400)
			hour = round(error.retry_after/3600)
			minute = round(error.retry_after/60)
			if day > 0:
				await ctx.send('Подождите '+str(day)+ " дней")
			elif hour > 0:
				await ctx.send('Подождите '+str(hour)+ " часов")
			elif minute > 0:
				await ctx.send('Подождите '+ str(minute)+" минут")
			else:
				await ctx.send(f'Подождите {error.retry_after:.2f} секунд')
		elif isinstance(error, CommandNotFound):
			return
		elif isinstance(error, MissingPermissions):
 			await ctx.send(error)
		elif isinstance(error, CheckFailure):
			await ctx.send(error)
		elif isinstance(error, NotOwner):
			await ctx.send(error)
		else:
			print(error) 

def setup(bot):
	bot.add_cog(OnCommandErrorCog(bot))
