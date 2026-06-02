from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8834745773:AAFYeKuFKwcvXkCbb-8Z1n4yNaYFd768C5Y"


async def guard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message

    if not msg:
        return

    print("=" * 80)
    print(msg.to_dict())
    print("=" * 80)

    try:
        # Комментарий под постом канала
        if (
            msg.reply_to_message
            and getattr(msg.reply_to_message, "is_automatic_forward", False)
        ):
            print("Комментарий к посту канала — оставляем")
            return

        # Обычное сообщение в группе обсуждения
        await msg.delete()
        print("Удалено обычное сообщение")

    except Exception as e:
        print("Ошибка:", e)


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL, guard)
)

print("Бот запущен")

app.run_polling(drop_pending_updates=True)
