from telethon import TelegramClient, events

api_id = 26732672
api_hash = 'aefa69d1670efd99dab0b567e73b1f10'
bot_token = '7124001656:AAF4sxCBBvTEYasfB2kdpfVmjGtcJETgbF8'
# ایجاد یک کلاینت جدید برای بات
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


# تعریف یک هندلر برای پیام‌های جدید
@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()  # دریافت اطلاعات فرستنده
    print(f"Message from {sender.username}: {event.text}"
          )  # نمایش پیام دریافتی در کنسول

    # پاسخ به پیام
    await event.reply('سلام! من یک بات تلگرام هستم. چگونه می‌توانم کمک کنم؟')


# اجرای بات
print("Bot is running...")
client.run_until_disconnected()
