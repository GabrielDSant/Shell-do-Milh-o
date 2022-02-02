#https://github.com/cherryWood55/Quiz-Game/blob/master/question.py
import random
import json
import time
import cowsay

varbanner = ['1', '2']

#iniciar o jogo com banner 
def banners():
    banner = open ('./banners/'+random.choice(varbanner)+'.txt', 'r')
    print (''.join([line for line in banner]))

#usuário entrando no "Menu" do jogo
def menu():
    pass

#Perguntar ao jogador qual o tema
def tema():
    pass

#mostrar perguntas ligadas ao tema do arquivo json
def pergunta(questão):
    cowsay.cow('Hello World')
    pass

#Função que responde a pergunta
def resposta(escolha):
    pass

#Verificar resposta
def corretor():
    pass

#Sistema de pontuação
def pontos():
    pass

#main
if __name__ == '__main__':
    banners()