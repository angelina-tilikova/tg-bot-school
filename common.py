async def resend_message(bot, message, text, keyboard=None):
    chatID = message.chat.id
    await message.delete()
    await bot.send_message(chat_id=chatID, text=text, reply_markup=keyboard)