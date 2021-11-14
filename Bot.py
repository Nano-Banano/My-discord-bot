import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
#updateinfo, info, ban, kick, help. 

@client.event

async def on_ready():
	print('КЛИЕНТ ПОДКЛЮЧЕНИЯ ЗАПУЩЕН')
	print('ПОПЫТКА ЗАПУСКА БОТА')
	print('ПОПЫТКА ЗАПУСКА: УДАЧНО')
	print('БОТ ЗАПУЩЕН')
	print('THE BOT HAS STARTED')
	
	await client.change_presence(status=discord.Status.online, activity=discord.Game('Бот взят сhttps://github.com/Nano-Banano/My-discord-bot|!help'))

@client.command(pass_context = True)
#информация
async def info(ctx):
	await ctx.send('Инфа о серваке')

#список команд. Не менять! А то криво работать будет! 
async def help(ctx):
	await ctx.send('Ban – Забанить пользователя.')

#кик
@client.command(pass_context = True)
@commands.has_permissions(kick_members = True)

async def kick(ctx, member: discord.Member, *, reason = None):
	await member.kick(reason = reason)
	await ctx.send(f'Участник {member.mention} был кикнут')
	
#бан

@client.command(pass_context = True)
@commands.has_permissions(ban_members = True)

async def ban(ctx, member: discord.Member, *, reason = None):

	await member.ban(reason = reason)
	await ctx.send(f'участник {member.mention} был забанен по причине: {reason}')
	
@client.command(pass_context = True)
@commands.has_permissions(ban_members = True)

#укажите токен в файле token.txt
token=open('token.txt', 'r').readline()
client.run(token)
