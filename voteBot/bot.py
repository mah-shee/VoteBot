import traceback

import discord

client = discord.Client()


# @client.event
# async def on_reaction_add(reaction, user):
#    author = reaction.message.author
#    await reaction.message.channel.send(f'{user}が{reaction.message}に{reaction.emoji}を付けました')


@client.event
async def on_message(message):
    if message.content.startswith("$hello"):
        if client.user != message.author:
            m = "おはようございます" + message.author.name + "さん！"
            await message.channel.send(m)

    elif message.content.startswith("ほめて"):
        if client.user != message.author:
            m = "やりましたね！" + message.author.name + "さん！"
            await message.channel.send(m)

    elif message.content.startswith("おやすみ"):
        if client.user != message.author:
            m = "おやすみなさい！" + message.author.name + "さん！"
            await message.channel.send(m)

    elif message.content.startswith("ぐぬぬ"):
        if client.user != message.author:
            m = "がんばって！" + message.author.name + "さんならいけます！"
            await message.channel.send(m)

    elif message.content.startswith("よろしい"):
        if client.user != message.author:
            m = "お役に立てて光栄です！" + message.author.name + "さん！"
            await message.channel.send(m)


@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "🙌" and reaction.count == 2:
        await reaction.message.add_reaction("😻")
