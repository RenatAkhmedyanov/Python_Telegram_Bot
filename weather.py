import requests
import datetime
from pprint import pprint
from config import open_weather_token
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def get_weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
       
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={update.message.text.split()[1]}&appid={open_weather_token}&units=metric'
    )
    data = r.json()
    
    city = data['name']
    cur_weather = data['main']['temp']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']

    await update.message.reply_text(f"---{datetime.datetime.now().strftime('%d-%m-%y %H:%M')}---\n"
            f'Погода в городе: {city}\nТемпература: {cur_weather}C°\n'
            f'Влажность: {humidity}%\nСкорость ветра: {wind} м/с')


    