import traceback
import discord

client = discord.Client()


#@client.event
#async def on_reaction_add(reaction, user):
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

    elif message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

    elif message.content.startswith("よろしい"):
        if client.user != message.author:
            m = "お役に立てて光栄です！" + message.author.name + "さん！"
            await message.channel.send(m)

    elif message.content.startswith("スイッチ"):
        msg = await message.channel.send("リアクションスイッチ")
        await msg.add_reaction('👈')
        await msg.add_reaction('👉')
        client.loop.create_task(check_reaction(msg))

@client.event
async def check_reaction(message):
    """
    指定のメッセージにリアクションがついたらメッセージを送る
    """
    while True:
        await client.wait_for('reaction_add')
        if message.reaction.emoji == '👈':
            await message.channel.send("戻る")

        elif message.reaction.emoji == '👉':
            await message.channnelsend("進む")

        else:
            pass

        await client.remove_reaction(message, \
        message.reaction.emoji, target_reaction.user)
