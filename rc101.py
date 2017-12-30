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

bot = commands.Bot(command_prefix="??")
bot.remove_command ('help')

@bot.event
async def on_ready():
    print("------------")
    print(" Logged in.")
    print("⭐Bot Ready⭐")
    print("------------")
    
@bot.command()
async def info(ctx):
    unique_members = set(bot.get_all_members())
    embed = discord.Embed(color = 0x6691D9, timestamp = datetime.datetime.utcnow(), title = "Cosmos Info", description = "Cosmos is a bot made only by Rapid, no more than a bit of help and some command examples from others. It is coded on an Android S7 on an application called Termux, by Rapid")
    embed.set_author(name = "All bot info and statistics", icon_url = "https://cdn.discordapp.com/attachments/379454585808617472/389255356636987394/20171206_140705.jpg")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/379454585808617472/389255356636987394/20171206_140705.jpg")
    embed.add_field(name = "Owner/Creator :spy:", value = "Rapid#0501")
    embed.add_field(name = "Made with <:Python:390560559113961472>", value = "Python Discord.py\nUsing Termux")
    embed.add_field(name = "Population :star:", value = "Servers: **{}".format(len(bot.servers)) + "**\n" + "Unique Members: **{}".format(len(set(bot.get_all_members()))) + "**\n" + "Unique Online: **{}".format(sum(1 for m in unique_members if m.status != discord.Status.offline)) + "**\n" + "Total Members: **{}".format(sum(len(s.members) for s in bot.servers)) + "**\n" + "Members Online:  **{}".format(sum(1 for m in bot.get_all_members() if m.status != discord.Status.offline)) + "**\n" + "Channels: **{}".format(len(set(bot.get_all_channels()))) + "**\n" + "Emojis: **{}".format(len(set(bot.get_all_emojis()))) + "**\n" + "Total Commands: **107**")
    embed.add_field(name = "Links :link:", value = "[Support Server]({})" .format("https://discord.gg/pDvJZEN") + "\n" + "[Invite Me]({})".format("https://discordapp.com/oauth2/authorize?client_id=385622427977121813&scope=bot&permissions=2146958591") + "\n" + "[DiscordBots.org]({})".format("https://discordbots.org/bot/385622427977121813"))
    embed.set_footer(text = "| © Cosmos ", icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
    await ctx.send(embed = embed)
    
cmds = "107"
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def help(ctx):
   user2send = ctx.message.author
   embed = discord.Embed(title = "Cosmos Commands", color = 0x6691D9, timestamp = datetime.datetime.utcnow(), description = "Cosmos's prefix is `?` If you need specific help on a command type `?help_<command>`")
   embed.set_author(name = '{} total commands'.format(cmds), icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
   embed.add_field(name = "Core Commands", value = "`help` | `info` | `invite` |  `msgdev` | `faq` | `betatesters` | `suggestion`")
   embed.add_field(name = "Utility Commands", value = "`messagessent` | `mail` | `invitegenerator` | `setup_starboard` | `charinfo` | `starboard` | `poll` | `serverinfo` | `channelinfo` | `userinfo` | `emojiinfo` | `roleinfo` | `avatar` | `servericon` | `urband` | `advert` | `timer`")
   embed.add_field(name = "Developer Commands", value = "`dm` | `announce` | `stop` | `servers` | `setwatching` | `setgame` | `setlistening` | `setstream`")
   embed.add_field(name = "Administrative Commands", value = "`nick` | `massnick` | `clearnicks` | `kick` | `ban` | `softban` | `mute` | `warn` | `gbans` | `addrole` | `removerole` | `createrole` | `deleterole` | `renamerole` | `clear`")
   embed.add_field(name = "Fun Commands", value = "`virus` | `ping` | `pong` | `rate` | `starterpack` | `coinflip` | `roll` | `choose` | `8ball` | `kill` | `hug` | `kiss` | `punch` | `slap` | `beatup` | `shoot` | `dicklength` | `amicool` | `dog` | `cat` | `neko` | `drake` | `salty` | `pun` | `yomomma` | `chucknorris` | `count` | `potatos` | `pick`")
   embed.add_field(name = "Miscellaneous Commands", value ="`embedsay` | `say` | `emojify` | `scramble` | `widentext` | `fingers` | `randomcommand` `gamertag` | `story` | `itsrapids` | `is` | `add` | `divide` | `multiply` | `subtract` | `power` |  `christmas` | `halloween` | `easter` | `saintpatrick` | `valentines`")
   embed.add_field(name = "MiniGame Commands", value = "`war` | `slots`")
   embed.add_field(name = "Read the manual Commands", value = "`rtfm` | `rtfm_async` | `rtfm_rewrite`")
   embed.add_field(name = "Discord.py Async HowTo's", value = "`tutBASICBOT` | `tutPING` | `tutSAY` | `tutCOINFLIP` | `tutTYPES` | `tutSERVERS` | `tutMEMBERS` | `tutCHANNELS` | `tutEMOJIS` | `tutERRORHANDLER` | `tutSETGAME` | `tutTERMUX`")
   embed.set_footer(text = "| © Cosmos ", icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
   embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
   await ctx.send_message(user2send, embed = embed)
   await ctx.send("**:white_check_mark: | I've sent you all my commands!**")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def war(ctx):
    cards = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
    member = ctx.message.author.name
    player = random.randint(2, 14)
    dealer = random.randint(2, 14)
    embed = await ctx.send(embed=discord.Embed(color=0x49bcff, description="**:shield: | Shuffling the cards...**"))
    await asyncio.sleep(1.0)
    await message.edit(embed, embed, embed=discord.Embed(color=0x49bcff, description="**:shield: | Shuffling the cards...\nDealing...**"))
    await asyncio.sleep(1.0)
    await message.edit(embed, embed=discord.Embed(color=0x49bcff, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**'))
    if int(player) > int(dealer):
        await asyncio.sleep(1.0)
        await message.edit(embed, embed=discord.Embed(color=0x84ba74, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}-----**\n`Player: ' + cards[player] + '`\n`Dealer: ' + cards[dealer] + '`\n**:tada: | You won {}!**'.format(ctx.message.author.name)))
    elif int(player) < int(dealer):
        await asyncio.sleep(1.0)
        await message.edit(embed, embed=discord.Embed(color=0xde0036, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**\n`Player: ' +cards[player] + '`\n`Dealer: ' + cards[dealer] + '`\n**:skull_crossbones: | You lost {}.**'.format(ctx.message.author.name)))
    else:
        await asyncio.sleep(1.0)
        player2 = random.randint(2, 14)
        player3 = random.randint(2, 14)
        player4 = random.randint(2, 14)
        dealer2 = random.randint(2, 14)
        dealer3 = random.randint(2, 14)
        dealer4 = random.randint(2, 14)
        if int(player4) > int(dealer4):
            await asyncio.sleep(1.0)
            await message.edit(embed, embed=discord.Embed(color=0x84ba74, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**\n`Player: ' + cards[player] + '`, ' + cards[player2] + ', ' + cards[player3] + ', `**Deciding Card: **' + cards[player4] + '`\nDealer: ' + cards[dealer] + '`, ' + cards[dealer2] + ', ' + cards[dealer3] + ', `**Deciding Card: **' + cards[dealer4] + '`\n**:tada: | You won {}!**'.format(ctx.message.author.name)))
        elif int(player4) < int(dealer4):
            await asyncio.sleep(1.0)
            await message.edit(embed, embed=discord.Embed(color=0xde0036, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**\n`Player: ' +cards[player] + '`, ' + cards[player2] + ', ' + cards[player3] + ', `**Deciding Card: **' + cards[player4] + '`\nDealer: ' +cards[dealer] + '`, ' + cards[dealer2] + ', ' + cards[dealer3] + ', `**Deciding Card: **' + cards[dealer4] + '`\n**:skull_crossbones: | You lost {}.**'.format(ctx.message.author.name)))
        else:
            await asyncio.sleep(1.0)
            await message.edit(embed, embed=discord.Embed(color=0xffc627, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**\n`Player: ' +cards[player] + '`, ' + cards[player2] + ', ' + cards[player3] + ', `**Deciding Card: **' + cards[player4] + '`\nDealer: ' +cards[dealer] + '`, ' + cards[dealer2] + ', ' + cards[dealer3] + ', `**Deciding Card: **' + cards[dealer4] + '`\n**:crossed_swords: | {}, it is a tie!**'.format(ctx.message.author.name)))

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

#👺👺👺👺👺👺👺ADMIN COMMANDS👺👺👺👺👺👺👺#
@bot.command()
async def nick(ctx, member : discord.Member, *,  name : str):
    if not ctx.message.author.server_permissions.manage_nicknames:
      return await ctx.send("**:x: | Insufficient permissions.**")
    await member.edit(nick, member, name)
    await ctx.send("**:white_check_mark: | Changed {}'s nickname to: `{}`**".format(member.name, name))

@bot.command()
async def kick(ctx, member : discord.Member, *,  reason: str = ""):
    if not ctx.message.author.server_permissions.kick_members:
      return await ctx.send("**:x: | Insufficient permissions.**")
    await member.kick(member)
    await ctx.send(member, "**You were kicked from {}!\nReason: {}\nAction by: {}**".format(ctx.message.server.name, reason, ctx.message.author.name))
    await ctx.send("**:white_check_mark: | Kicked {}, reason: `{}`**".format(member.name, reason))
    
if not os.environ.get('TOKEN'):
    print("no token found!")
bot.run(os.environ.get('TOKEN').strip('"'))
