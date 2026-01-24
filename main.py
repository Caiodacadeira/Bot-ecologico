import discord
from bot_logic import RS
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def Rs(ctx, R: int):
  await ctx.send(RS(R))

bot.run('token')
