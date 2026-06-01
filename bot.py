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
    try:
        msg = update.message

        if not msg:
            return

        # Сообщение канала не трогаем
        if msg.sender_chat:
            return

        # Комментарий к посту канала
        if msg.message_thread_id:
            return

        # Обычное сообщение в группе удаляем
        await msg.delete()

    except Exception as e:
        print(e)


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL, guard)
)

app.run_polling()
