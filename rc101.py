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
    
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def help(ctx):
    embed=discord.Embed(color=0xffe502, title="Commands", timestamp=datetime.datetime.utcnow(), description="Welcome to Cosmos Alpha, cleaner, and better. The prefix is `/`, using the latest library of Python, `rewrite`!")
    embed.add_field(name="Core", value="```info | help```")
    embed.add_field(name="Utilities", value="```Coming soon...```")
    embed.add_field(name="Administrative", value="```Coming soon...```")
    embed.add_field(name="Fun/Misc", value="```ping | pong```")
    embed.add_field(name="NSFW", value="```boobs | butts```")
    embed.set_footer(text="Cosmos Alpha ")
    await ctx.send(embed=embed)
    
@bot.command()
async def botinfo(ctx):
    embed=discord.Embed(color=0xffe502, title="Information", timestamp=datetime.datetime.utcnow(), description="Cosmos Alpha, is cleaner, and better. This bot was re-made in the need of using the latest Python library. Cosmos used Async, thr older out of date library.")
    embed.add_field(name="Written With", value="Python.py (Rewrite Library)")
    embed.add_field(name="Creator", value="Rapid#0501")
    embed.set_footer(text="Cosmos Alpha ")
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    time=time.time()
    ping = time.time() - pingtime
    await ctx.send("**Pong! `%.01f seconds`**"%ping)
    
@bot.command()
async def pong(ctx):
    time=time.time()
    ping = time.time() - pingtime
    await ctx.send("**Ping! `%.01f seconds`**"%ping)
   
@bot.command()
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
    
@bot.command()
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
   
@bot.command()
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

if not os.environ.get('TOKEN'):
    print("no token found!")
bot.run(os.environ.get('TOKEN').strip('"'))
