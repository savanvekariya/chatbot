from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import winspeech
import os

bot=ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data=open('C:/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    bot.train(data)

while True:
    message = input('You :')
    winspeech.say(message)
    if message.strip()!='bye':
        reply = bot.get_response(message)
        print('Chatbot :', reply)
        winspeech.say(reply)
    if message.strip()=='bye':
        print('Chatbot : bye, see you again.')
        winspeech.say_wait("bye,see you again")
        break
