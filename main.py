import telegram.ext
import os
from telegram import InlineKeyboardButton , InlineKeyboardMarkup

TOKEN ='your telegram bot token '

web_url = 'https://msnsale.rf.gd'

def start(update,context):
    chat_id = update.message.chat_id
    referral_id = context.args[0] if context.args else None

    web_button_url = f"{web_url}?id={referral_id}&user={chat_id}"
    keyboard = [[InlineKeyboardButton("Visit Website", url=web_button_url)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(chat_id=chat_id, text="message text", reply_markup=reply_markup)
    context.bot.send_message(chat_id='5204205237', text=f'UserId:- <code>{chat_id}</code>', parse_mode='HTML')

def handle_message(update, context):
    chat_id = update.message.chat_id

    web_button_url = f"{web_url}?id=null&user={chat_id}"
    keyboard = [[InlineKeyboardButton("Visit Website", url=web_button_url)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(chat_id=chat_id, text="message text", reply_markup=reply_markup)

updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start',start))
dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text,handle_message))

updater.start_polling()
updater.idle()