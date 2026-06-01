async def guard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        msg = update.message

        if not msg:
            return

        # Сообщение канала или системное сообщение не трогаем
        if msg.sender_chat:
            return

        # Комментарий к посту канала
        if msg.message_thread_id:
            return

        # Обычное сообщение пользователя удаляем
        await msg.delete()

    except Exception as e:
        print(e)
