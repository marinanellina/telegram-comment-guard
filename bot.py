from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "ТВОЙ_ТОКЕН"


async def guard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message

    if not msg:
        return

    print(msg.to_dict())

    # Если это комментарий к посту канала — оставляем
    if getattr(msg, "is_automatic_forward", False):
        print("Комментарий к посту канала")
        return

    # Удаляем обычное сообщение
    try:
        await msg.delete()
        print("Удалено обычное сообщение")
    except Exception as e:
        print("Ошибка удаления:", e)


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL, guard)
)

app.run_polling(drop_pending_updates=True)
