import discord
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

bot = discord.Client()
ddb = DiscordComponents(bot)

@bot.event
async def on_ready():
    print("Ready!")
    
@bot.event
async def on_message(message):
    if message.content.startswith('!welcome'):
        embed=discord.Embed(title="yude.jp の Discord サーバーへようこそ!", url="https://yude.jp", description="Welcome to yude.jp Discord server!", color=0xffa3f0)
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/550309736214691840/2e18e529b75fc216f970b59a067bd737.webp?size=128")
        embed.add_field(name="💫 概要", value="このサーバーの目的は特にありません。\n招待リンク: [discord.gg/X6srY7X](https://discord.gg/X6srY7X)\nMember ロールは Dyno ボットにより参加時に自動的に付与されます。", inline=False)
        embed.add_field(name="📕 ルール", value="1. 過激すぎる発言をしないでください。\n2. チャットスパムを行わないでください。", inline=False)
        embed.add_field(name="👥 GitHub Organization", value="[こちら](https://yudejp-github-org.herokuapp.com/) からあなたのアカウントに yude.jp の GitHub Organization の招待を送信することができます。", inline=False)
        await message.channel.send(embed=embed,components=[
                Button(style=ButtonStyle.URL, label="Twitter", url="https://twitter.com/yudejp"),
                Button(style=ButtonStyle.URL, label="GitHub Organization", url="https://github.com/yudejp"),
                Button(style=ButtonStyle.URL, label="LINE オープンチャット", url="https://line.me/ti/g2/mi36ZEsJkIo9BLqYg1sQFg"),
            ])

bot.run("token")
