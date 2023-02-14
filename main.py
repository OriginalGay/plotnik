import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def skibidi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text= '420')

if __name__ == '__main__':
    application = ApplicationBuilder().token('6255294638:AAEpSF3f_7Y-DUqYGc16vcKexeIFojHEEP8').build()

    start_handler = CommandHandler('start', start)
    skibidi_handler = CommandHandler('skibidi', skibidi)

    application.add_handler(skibidi_handler)
    application.add_handler(start_handler)

    application.run_polling()
