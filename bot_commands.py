from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time
import datetime
import random
import os




async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hello\n/time\n/help\n/calc\n/days_to_NY\n/weather Название города\n/cats')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{time.asctime()}')

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Ответ: {eval(update.message.text.split()[1])}')

async def days_to_NY_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.today()
    NY = datetime.datetime(2024, 1, 1)
    d = NY-now  
    await update.message.reply_text(f'До нового года осталось дней: {d.days}.')

async def cats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = open('cats/' + random.choice(os.listdir('cats')), 'rb')
    await update.message.reply_photo(photo)
    
