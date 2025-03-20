import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=kr&units=metric"
    response = requests.get(url)

    print(response.status_code, response.json())

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']

        if "맑" in weather_description:
            return "맑음"
        elif "구름" in weather_description:
            return "흐림"
        elif "비" in weather_description:
            return "비"
        elif "눈" in weather_description:
            return "눈"
        else:
            return "알 수 없음"
    else:
        return None

API_KEY = "48538c03b6bb2ec8fe75ebeee2fc3e31"  #OpenWeatherMap API
CITY = "Seoul"

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print(f'{client.user}에 로그인하였습니다.')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('날씨 예측'))

@client.event
async def on_message(message):
    if message.content == "안녕":
        await message.channel.send("안녕하세요, {} {}".format(message.author, message.author.mention))

    if message.content == "날씨":
        await message.channel.send("오늘의 날씨는 {}입니다.".format(get_weather(API_KEY, CITY)))

client.run('MTM1MTQwMjgzOTU4NjYzNTg5MQ.GCRrIt.DROAv2SuoQcnDkuOeKCfoKLhRA7SOaBes20Yz4')
