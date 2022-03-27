#https://github.com/cherryWood55/Quiz-Game/blob/master/question.py
from cgi import print_arguments
import random
import json
import cowsay

varbanner = ['1', '2', '3']
temas = ['Red', 'Blue']

#Tentando criar uma lista de numeros strings DEU CERTO DEUS MUITO OBRIGADO NUNCA FUI TRSTE

ListaDeNumero = range(1, 2)

lista_questoes = [str(x) for x in ListaDeNumero]

#Sorteio da questão
def sorteio():
    tei = random.choice(lista_questoes)
    return tei

#iniciar o jogo com banner 
def banners():
    banner = open ('./banners/'+random.choice(varbanner)+'.txt', 'r')
    print (''.join([line for line in banner]))
    sorteio()
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
def tema(arquivo):
    with open ('./temas/'+arquivo+'.json', 'r') as temajson:
        cow = cowsay.cow(json.load(temajson)[sorteio()]["questao"])
        if cow:
            pergunta(cow)

#mostrar perguntas ligadas ao tema do arquivo json
def pergunta(questão):
    print(questão)
    resposta_user = input("Espero que você tenha estudado... Qual é a correta ?: ")
    if resposta_user:
        resposta(resposta_user)
#Função que responde a pergunta
def resposta(escolha):
        if escolha == "ADD arquivo json e verificar resposta to com sono":
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