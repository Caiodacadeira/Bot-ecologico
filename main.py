import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='r!', intents=intents)

@bot.command()
async def Rs(ctx, R:int):
  await ctx.send()

bot.run('token')
