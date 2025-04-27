from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = 8070225155:AAGQ-0JPuzRnR2Yf5gCYQRwQInbIWg3RM38

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salom! 👋 Men sizga yordam beraman.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if "isming nima" in text:
        await update.message.reply_text("🤖 Mening ismim ChatBot!")
    elif "qandaysan" in text:
        await update.message.reply_text("😊 Yaxshiman! Siz-chi?")
    elif "nima qilayapsan" in text:
        await update.message.reply_text("💬 Savollaringizga javob bermoqdaman.")
    elif "sen kimsan" in text:
        await update.message.reply_text("🤖 Men sun'iy intellekt yordamchisiman.")
    elif "xayr" in text or "hayr" in text:
        await update.message.reply_text("👋 Xayr! Yana ko‘rishguncha!")
    else:
        await update.message.reply_text("❓ Kechirasiz, bu savolga javob bera olmayman.")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("✅ Bot ishga tushdi!")
app.run_polling()
