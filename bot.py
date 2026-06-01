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

    # Сообщение не является комментарием к посту канала
    if not msg.message_thread_id:
        try:
            await context.bot.delete_message(
                chat_id=msg.chat_id,
                message_id=msg.message_id
            )
            print("Удалено сообщение:", msg.text)
        except Exception as e:
            print("Ошибка удаления:", e)


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL, guard)
)

print("БОТ ЗАПУЩЕН")

app.run_polling(drop_pending_updates=True)
