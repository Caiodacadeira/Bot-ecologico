import discord
from bot_logic import rs_funcao
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def rs(ctx, R: int):
  await ctx.send(rs_funcao(R))

@bot.command()
async def ajuda(ctx):
  ajuda_texto = (
    "🌿 números disponíveis no comando rs:\n"
    "1-10: Retorna a explicação do R correspondente.\n"
    "11: Explica a existência dos Rs da sustentabilidade.\n"
    "12: Mostra todos os Rs da sustentabilidade.\n\n"
    "Exemplo de uso: !rs 3"
  )
  await ctx.send(ajuda_texto)

bot.run('token')
