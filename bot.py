import random
import discord
from discord.ext import commands

with open('bot.txt') as bot:
    auth = bot.readlines()
auth = [x.strip() for x in auth]

client = commands.Bot(command_prefix = '!')

@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping {round(client.latency * 1000)}ms')

@client.command()
async def delete(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def coinflip(ctx):
    responses = ['Heads', 'Tails']
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def commands(ctx):
    await ctx.send("!hello, !ping, !delete, !coinflip")
client.run(auth[0])