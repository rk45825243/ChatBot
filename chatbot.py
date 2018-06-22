from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot("Emma")
bot.set_trainer(ListTrainer)

for files in os.listdir(
        'C:/Users/user/PycharmProjects/ChatBot/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english'):
    chats = open(
        'C:/Users/user/PycharmProjects/ChatBot/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files
        , 'r').readlines()
    bot.train(chats)

while True:
    request = input('You:')
    response = bot.get_response(request)
    print('Emma:', response)
