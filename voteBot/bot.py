import traceback
import discord

client = discord.Client()

# async def send2developer(text):
#     """ 開発者にDMを送る """
#     # DEVELOPER_ID に自分のユーザIDを入れてください
#     developer = client.get_user(DEVELOPER_ID)
#     dm = await developer.create_dm()
#     await dm.send(text)
# 
# 
# @client.event
# async def on_ready():
#     """ 起動時のイベントハンドラ """
#     text = f'Logged on as {client.user}!'
#     await send2developer(text)
# 
# 
# @client.event
# async def on_message(message):
#     """ メッセージ受信時のイベントハンドラ """
#     try:
#         if message.author != client.user:  # bot自身の発言には反応しない
#             text = 'Message from {0.author}: {0.content}'.format(message)
#             await send2developer(text)
#     except Exception:  # エラー発生時にはトレースバックがDMで送られてくる
#         await send2developer(traceback.format_exc())


@client.event
async def on_reaction_add(reaction, user):
    author = reaction.message.author
    await reaction.message.channel.send(f"{user} さんがめっちゃリアクションをしました")


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
