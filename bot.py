from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "ВСТАВИМ_ПОТОМ_ТОКЕН"

async def debug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        print("=" * 80)
        print(update.to_dict())
        print("=" * 80)
    except Exception as e:
        print(e)

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL, debug)
)

app.run_polling()
