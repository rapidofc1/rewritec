import unicodedata
import youtube_dl
import pyowm
import traceback
import os
import sys
import sqlite3
import discord
from discord.ext import commands
import random
import asyncio
from datetime import datetime
import aiohttp
import json
import requests
import datetime
import time
from bs4 import BeautifulSoup
import ftfy

bot = commands.Bot(command_prefix="/")
bot.remove_command('help')

@bot.event
async def on_ready():
    print("------------")
    print(" Logged in.")
    print(bot.user.name)
    print("------------")
    
@bot.command()#1
@commands.cooldown(1, 10, commands.BucketType.user)
async def hellp(ctx):
    embed=discord.Embed(color=0xffe502, title="Cosmos Alpha", timestamp=datetime.datetime.utcnow(), description="Welcome to Cosmos Alpha, cleaner, and better. The prefix is `/`, and I use a new library of Python, `rewrite`!")
    embed.add_field(name="Core", value="```info () help ()```")
    embed.add_field(name="Utilities", value="```Coming soon...```")
    embed.add_field(name="Administrative", value="```Coming soon...```")
    embed.add_field(name="Fun/Misc", value="```Coming soon...```")
    embed.add_field(name="NSFW", value="```boobs () butts```")
    embed.set_footer(text="Cosmos Alpha ")
    await ctx.send(embed=embed)

@bot.command()#2
async def boobs(ctx):
    if not ctx.channel.is_nsfw():
      await ctx.send("**This channel is not marked as NSFW.**")
      return
    """Random boobies!"""
    api_base = 'http://api.oboobs.ru/boobs/'
    number = random.randint(1, 10303)
    url_api = api_base + str(number)
    async with aiohttp.ClientSession() as session:
        async with session.get(url_api) as data:
            data = await data.json()
            data = data[0]
    image_url = 'http://media.oboobs.ru/' + data['preview']
    em = discord.Embed(color=0xff02e9)
    em.set_author(name="Random NSFW Image")
    em.set_image(url=image_url)
    em.set_footer(text=f"Requested by {ctx.message.author.name}")
    await ctx.send(embed=em)
    
@bot.command()#3
async def butts(ctx):
    if not ctx.channel.is_nsfw():
      await ctx.send("**This channel is not marked as NSFW.**")
      return
    """Random butts!"""
    api_base = 'http://api.obutts.ru/butts/'
    number = random.randint(1, 4296)
    url_api = api_base + str(number)
    async with aiohttp.ClientSession() as session:
        async with session.get(url_api) as data:
            data = await data.json()
            data = data[0]
    image_url = 'http://media.obutts.ru/' + data['preview']
    em = discord.Embed(color=0xff02e9)
    em.set_author(name="Random NSFW Image")
    em.set_image(url=image_url)
    em.set_footer(text=f"Requested by {ctx.message.author.name}")
    await ctx.send(embed=em) 
   
@bot.command()#4
@commands.cooldown(1, 10, commands.BucketType.user)
async def slots(ctx):
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)

    if (a == b ==c):
        message = f':tada: | You won {ctx.message.author.name}!'
    elif (a == b) or (a == c) or (b == c):
        message = f':hotsprings: | {ctx.message.author.name}, you almost won, 2/3!'
    else:
        message = f':flag_white: | You lost {ctx.message.author.name}.'

    embed = await ctx.send(embed=discord.Embed(color=0xffffff, description=f'**:slot_machine: | {ctx.message.author.name} rolled the slots...**'))
    await asyncio.sleep(1.0)
    await message.edit(embed, embed=discord.Embed(color=0xffffff, description=f'**:slot_machine: | {ctx.message.author.name} rolled the slots...\nSpinning...**'))
    await asyncio.sleep(1.0)
    await message.edit(embed, embed=discord.Embed(color=0xffffff, description=f'**:slot_machine: | {ctx.message.author.name} rolled the slots...\nSpinning...\n------{ctx.message.author.name}------**'))
    await asyncio.sleep(1.0)
    await message.edit(embed, embed=discord.Embed(color=0xffffff, description=f'**:slot_machine: | {ctx.message.author.name} rolled the slots...\nSpinning...\n------{ctx.message.author.name}------\n`{a} | {b} | {c}`\n{message}**'))

#👺👺👺👺👺👺👺ADMIN COMMANDS👺👺👺👺👺👺👺#
@bot.command()#5
async def nick(ctx, member : discord.Member, *,  name : str):
    if not ctx.message.author.server_permissions.manage_nicknames:
      return await ctx.send("**:x: | Insufficient permissions.**")
    await member.edit(nick, member, name)
    await ctx.send("**:white_check_mark: | Changed {}'s nickname to: `{}`**".format(member.name, name))
    
@bot.command()#6
async def kick(ctx, member : discord.Member, *,  reason: str = ""):
    if not ctx.message.author.server_permissions.kick_members:
      return await ctx.send("**:x: | Insufficient permissions.**")
    await member.kick(member)
    #await ctx.send(member, "**You were kicked from {}!\nReason: {}\nAction by: {}**".format(ctx.message.server.name, reason, ctx.message.author.name))
    await ctx.send("**:white_check_mark: | Kicked {}, reason: `{}`**".format(member.name, reason))
    
if not os.environ.get('TOKEN'):
    print("no token found!")
bot.run(os.environ.get('TOKEN').strip('"'))
