import os
from telegram.ext import Application

TOKEN = os.getenv("BOT_TOKEN")

app = Application.builder().token(TOKEN).build()

print("BOT STARTED")

app.run_polling()
