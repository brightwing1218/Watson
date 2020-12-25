import discord
import os

client = discord.Client()

@client.event
async def on_ready(): #봇이 구동할 준비가 되었을 때 하단 명령 실행
    print(client.user.id)
    print("ready")

@client.event
async def on_message(message):#누군가 메시지를 보냈을 때 하단 명령 실행
    if message.content.startswith("안녕"):
        await message.channel.send("반가워")


access_token = os.environ["BOT_TOKEN"]        
client.run(access_token)
