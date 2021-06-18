import update as update
from telegram import *
from telegram.ext import *

bot = Bot("1744819316:AAGh9vwR5CwVFs6m_Bts1b_dxn8qfPm6PRU")
#print(bot.get_me())
updater=Updater("TOKEN KEY",use_context=True)  #Token key apply here

dispatcher=updater.dispatcher

def test_function(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="Hello Coder, great to have you on board! Let's get started: type /help to get the list of all the possible commands."

    )

start_value=CommandHandler('start',test_function)
dispatcher.add_handler(start_value)


def test(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="Here are the basic list of commands that you can use:                            1)/sites - To get the information on upcoming & running contests from all the available websites.                                                                      2)/more - Connect with the community & the developers of this bot!                                                                                                                       3)/contribute - To know more about contributing to this project."


    )

start_value1=CommandHandler('help',test)
dispatcher.add_handler(start_value1)

def test2(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="Here are the websites from which the contests will be listed from:                                                        1. Codeforces                                                                                           /cf_contests - To get all the upcoming contests on CodeForces.                                                                                  2. CodeChef                                                                                          /cc_contests - To get all the upcoming contests on CodeChef.                                                                                                             3. Atcoder                                                                                                    /ac_contests - To get all the contests from AtCoder."


    )

start_value3=CommandHandler('sites',test2)
dispatcher.add_handler(start_value3)

def test3(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="/cf_contests                                                                                                              https://codeforces.com/contests"


    )

start_value4=CommandHandler('cf_contests',test3)
dispatcher.add_handler(start_value4)


def test4(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="/cc_contests                                                                                                              https://www.codechef.com/contests"


    )

start_value5=CommandHandler('cc_contests',test4)
dispatcher.add_handler(start_value5)


def test5(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="/ac_contests                                                                                                              https://atcoder.jp/"


    )

start_value6=CommandHandler('ac_contests',test5)
dispatcher.add_handler(start_value6)


def test6(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="/aboutdevloper :-  To know more about the developers!"


    )

start_value7=CommandHandler('more',test6)
dispatcher.add_handler(start_value7)


def test7(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="Portfolio :- https://abhishektyagi2912.github.io/abhishek-portfolio/"


    )

start_value8=CommandHandler('aboutdevloper',test7)
dispatcher.add_handler(start_value8)


def test8(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="Contribute to this project to make it bigger and better :)                                                                      Repo link:https://github.com/abhishektyagi2912/Spike                                                                                                                                                                                                   Make Open Source Programming fun and Happy Developing! 👩‍💻👨‍💻"


    )

start_value9=CommandHandler('contribute',test8)
dispatcher.add_handler(start_value9)


updater.start_polling()

