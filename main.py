import openai
import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO

)

openai.api_key = ''
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hey!")

async def number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text= '8')

async def echo(update, context):
    text = update.message.text
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=text,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )
    message = response.choices[0].text.strip()
    await update.message.reply_text(message)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")




if __name__ == '__main__':
    application = ApplicationBuilder().token('').build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    start_handler = CommandHandler('start', start)
    number_handler = CommandHandler('number', number)

    application.add_handler(number_handler)
    application.add_handler(start_handler)
    application.add_handler(caps_handler)
    application.add_handler(unknown_handler)
    application.add_handler(echo_handler)

    application.run_polling()
