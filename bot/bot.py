#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters #import modules
from planet import get_sign_by_planet
from wordcount import wordcount

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

def show_error(bot, update, error):
    print(error)

def get_sign(bot, update, args):
    planet_name = args[0]
    print('Вызван /planet')
    bot.sendMessage(update.message.chat_id, get_sign_by_planet(planet_name))

def count_words(bot, update, args):
    print('Вызван /wordcount')
    bot.sendMessage(update.message.chat_id, wordcount(args))

def greet_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')
    
def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)
    
def main():
    updater = Updater('346621438:AAGJqm_SpuDvYtnpQj-PGF8lTbThTRRO3uo') #create an object of class
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_handler(CommandHandler('planet', get_sign, pass_args=True))
    dp.add_handler(CommandHandler('wordcount', count_words, pass_args=True))

    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()


main()
