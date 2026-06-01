import os

from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")


async def guard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.to_dict())


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL, guard)
)

app.run_polling()
