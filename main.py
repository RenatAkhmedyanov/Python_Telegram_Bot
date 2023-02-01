from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from weather import *



app = ApplicationBuilder().token("").build()
print('server start')

app.add_handler(CommandHandler("hello", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler("days_to_NY", days_to_NY_command))
app.add_handler(CommandHandler("weather", get_weather))
app.add_handler(CommandHandler("cats", cats_command))


app.run_polling()

