from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    "Job",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')

# Treinar Bot
treinar_bot = True  # True para treinar o bot (só é necessário uma vez)
if treinar_bot:
    treino = ChatterBotCorpusTrainer(chatbot)
    treino.train('chatterbot.corpus.Portuguese')


if __name__ == '__main__':
    while True:
        try:
            bot_resposta = chatbot.get_response(input())
            print(bot_resposta)

        except(KeyboardInterrupt, EOFError, SystemExit):
            print('Bate papo finalizado!')
            break
