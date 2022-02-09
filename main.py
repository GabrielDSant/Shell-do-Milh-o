#https://github.com/cherryWood55/Quiz-Game/blob/master/question.py
import random
import json
from traceback import format_list
import cowsay

varbanner = ['1', '2', '3']
temas = ['Red', 'Blue']
questao_selecionada = range(1, 2)




#iniciar o jogo com banner 
def banners():
    banner = open ('./banners/'+random.choice(varbanner)+'.txt', 'r')
    print (''.join([line for line in banner]))
    menu()
    
#usuário entrando no "Menu" do jogo
def menu():
    print("Bem-vindo ao shell do milhão :)\nPara o jogo iniciar escolha o tema da vez.\n \n|Red| para perguntas focadas no red team.\n|Blue| para perguntas focadas no blue team.")
    Escolha_do_tema = input("Tema escolhido: ")
    if Escolha_do_tema in temas:
        tema(Escolha_do_tema)
    else:
        print("tema não encontrado")

#Perguntar ao jogador qual o tema 
#ele retorna o json do tema para a função tema...
def tema(arquivo):
    with open ('./temas/'+arquivo+'.json', 'r') as temajson:
        opçoesjson = json.load(temajson)
        print(cowsay.cow(opçoesjson[random.choice('"'+questao_selecionada+'"')]["questao"]))
    #forma de chamar bagulho do json é aqui em cima em to com sono

#mostrar perguntas ligadas ao tema do arquivo json
def pergunta(questão):
    pass
#Função que responde a pergunta
def resposta(escolha):
    pass

#Verificar resposta"""""
def corretor():
    pass

#Sistema de pontuação
def pontos():
    pass

#main
if __name__ == '__main__':
    banners()