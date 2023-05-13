import discord
import requests
import asyncio

intents = discord.Intents.all()
client = discord.Client(intents=intents)


async def update_nickname():
    while True:
        # change this according to whichever token you want to track, read README.md for more info
        response = requests.get(
            "https://api.dexscreener.io/latest/dex/pairs/polygon/0xfb0bc232CD11dBe804B489860c470B7f9cc80D9F")
        data = response.json()
        for pair in data['pairs']:
            priceNative = pair['priceNative']
        nickname = f"${priceNative}"
        guild = client.guilds[0]
        member = guild.me
        await member.edit(nick=nickname)
        await asyncio.sleep(300)  # 5 minutes


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    client.loop.create_task(update_nickname())

client.run("TOKEN")  # put your own discord bot token here
