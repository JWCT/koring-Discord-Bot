import discord, datetime
import random
import asyncio
token = "[봇 토큰은 제외임 ㅅㄱ]"
client = discord.Client()

@client.event
async def on_ready():
    print("봇 준비 완료!")
    print(client.user)
    print("============================")
    
@client.event
async def on_message(message):
    if message.content == "!안녕":
        await message.channel.send("네 안녕하세요!")

    if message.content == "!임베드테스트":
        embed = discord.Embed(colour=discord.Colour.red(), title="제목", description="설명")
        await message.channel.send(embed=embed)

    if message.content.startswith(f"!채널메세지"):
        ch = client.get_channel(int(message.content[7:25]))
        await ch.send(message.content[26:])

    if message.content == '!내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임 : {user.name} / {user.id} / {user.display_name}")
        await message.channel.send(message.author.avatar_url)

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제 완료!")

    if message.content == "!복권":
        await message.channel.send(random.choice(['꽝!', '꽝!', '꽝!', '꽝!', '꽝!', '꽝!', '꽝!', '꽝!', '꽝!', '축하합니다 10분의 1를 뚫으셨군요!']))

    if message.content == "!타이머 10초":
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}, 10초가 지났어요! 땡땡땡!")

    if message.content == "!타이머 1분":
        await asyncio.sleep(60)
        await message.channel.send(f"{message.author.mention}, 1분가 지났어요! 땡땡땡!")

    if message.content.startswith("!만드신사람"):
        embed = discord.Embed(title="코링님을 만들어 주신 사람입니다.", description="저를 만들어 주신분이십니다!", color=0xAAFFFF) 
        embed.add_field(name="닉네임", value="애푸르스박#3562", inline=False)
        embed.add_field(name="ID", value="807500935928610847", inline=False)

    if message.content == "!초대하기":
        embed=discord.Embed(title="코링! 초대링크", description = "여기입니다!(https://discord.com/api/oauth2/authorize?client_id=810350086860308500&permissions=8&scope=bot) 이 링크를 눌러 저를 초대하세요.", color=0x00ff00)
        await message.channel.send(embed=embed)

client.run(token)
