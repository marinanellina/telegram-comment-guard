from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8834745773:AAFYeKuFKwcvXkCbb-8Z1n4yNaYFd768C5Y"


async def guard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.to_dict())

    await update.message.reply_text(
        "Привет! Бот работает."
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL, guard)
)

app.run_polling(drop_pending_updates=True)
