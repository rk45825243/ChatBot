from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot("drake")  #changing chatbot name
bot.set_trainer(ListTrainer)

for files in os.listdir(
        'C:/Users/user/PycharmProjects/ChatBot/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english'):
    chats = open(
        'C:/Users/user/PycharmProjects/ChatBot/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files
        , 'r').readlines()
    bot.train(chats)

while True:
    user_request = input('you:')  #changing request variable to user_request
    feedback = bot.get_feedback(user_request)  #changing variable response to feedback
    print('drake:', feedback)  #changing name of chatbot entered and changing variable entered
