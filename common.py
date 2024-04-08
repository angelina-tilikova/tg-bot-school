async def resend_message(bot, message, text, keyboard=None):
    chatID = message.chat.id
    await message.delete()
    await bot.send_message(chat_id=chatID, text=text, reply_markup=keyboard, disable_web_page_preview=False)
    
async def resend_message_without_preview(bot, message, text, keyboard=None):
    chatID = message.chat.id
    await message.delete()
    await bot.send_message(chat_id=chatID, text=text, reply_markup=keyboard, disable_web_page_preview=True)