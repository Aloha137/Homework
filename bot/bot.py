#!/usr/bin/python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters #import modules


def show_error(bot, update, error):
    print(error)
    
def greet_user(bot, update):
    print('Вызван /start')
    print(vars(update))
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')
    
def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)
    
def main():
    updater = Updater('346621438:AAGJqm_SpuDvYtnpQj-PGF8lTbThTRRO3uo') #create an object of class
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))


    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()


main()
