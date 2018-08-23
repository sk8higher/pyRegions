##
## Copyright (c) 2018 Nelly Simkova.
##
## This file is part of pyRegions
## (see https://github.com/sk8higher/pyRegions).
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program. If not, see <http://www.gnu.org/licenses/>.
##

import telebot
from bottoken import bot_token
from ru import ruRegions

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 'Это бот, который показывает место по автомобильному региону. Введите цифру, и бот '
                 'подскажет, из какого региона России данная машина.')


@bot.message_handler(func=lambda m: True)
def reply(message):
    if message.text in ruRegions:
        bot.reply_to(message, ruRegions.get(message.text))
    else:
        bot.reply_to(message, 'Такого региона не существует.')


def main():
    bot.polling()


if __name__ == '__main__':
    main()

