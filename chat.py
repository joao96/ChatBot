# responsável por permitir que uma lista de strings seja utilizada no processo de aprendizagem do Bot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import os

chatbot = ChatBot('Campusito')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.portuguese"
)

trainer2 = ListTrainer(chatbot)

for arq in os.listdir('arquivos'):
  chats = open('arquivos/' + arq, 'r').readlines()
  # Por padrão, cada resposta se refere ao item anterior da lista.
  trainer2.train(chats)


print('Oie! Eu sou o Campusito, a foca do Campus Online. Prazer é todo meu, migo! Muito \
bom ver você por aqui, mas sad news: nosso jornal está em período de transição no momento \
e voltamos a ativa no dia DIA_DE_RETORNO, só que nada vai me impedir de ouvir tudo o \
que você tem a dizer e responder assim que possível! Me diz aí o que você manda!')

print('- Sugestões.')
print('- Problemas.')
print('- Correções.')
print('- Reclamações.')

while True:
    pergunta = input("Usuário: ")
    resposta = chatbot.get_response(pergunta)
    if float(resposta.confidence) > 0.1:
        print('Campusito:', resposta)
    else:
        print('Campusito: Ainda não sei responder esta pergunta')

# Vale ressaltar que as perguntas e respostas do nosso ChatBot vão sendo armazenadas em um banco de dados SQLite criado automaticamente.         
# Um outro ponto importante é que o processo de aprendizado é um pouco lento, então você terá que conversar alguns minutos com seu 
# ChatBot até que ele aprenda novas perguntas e suas respectivas respostas.

# Nosso ChatBot será inicializado e nós podemos trocar mensagens com ele. Após alguns minutos de conversa, você 
# perceberá que o ChatBot fará perguntas que não estão cadastradas em nossa lista conversa. Estas perguntas são aprendidas 
# com o tempo e armazenadas no banco de dados