from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot("Emma")
bot.set_trainer(ListTrainer)



while True:
    request = input('You:')
    response = bot.get_response(request)
    print('Emma:', response)
