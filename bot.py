import os

from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")


async def guard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if not msg:
        return

    # Сам канал не трогаем
    if msg.sender_chat:
        return

    # Комментарий под постом канала
   if msg.message_thread_id:
    try:
        print("Пытаюсь удалить")
        print("chat_id =", msg.chat_id)
        print("message_id =", msg.message_id)

        await context.bot.delete_message(
            chat_id=msg.chat_id,
            message_id=msg.message_id
        )

        print("Комментарий удалён")

    except Exception as e:
        print("Ошибка:", repr(e))


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL, guard)
)

app.run_polling()
