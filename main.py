import discord
from bot_logic import rs_funcao
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def rs(ctx, R: int):
  await ctx.send(rs_funcao(R))

bot.run('token')
