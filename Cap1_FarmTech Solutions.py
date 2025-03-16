import os, sys
from tkinter import Tk
from time import sleep
from math import pi


dados = {'CULTURA':['MILHO', 'SOJA', 'SOJA'],
        'AREA':[210201, 520002, 2010203],
        'INSUMOS':[431214, 345344, 546456]}

# MENU
# Boas Vindas
# print('Bem vindo ao aplicativo da FarmTech Solution\n\n')



#FUNÇÃO DESTINADA A EXIBIÇÃO DE DADOS
def exibir_dados(dicionario):

    # Montando cabeçario
    print('\n|INDEX|CULTURA|-----AREA-----|-----INSUMOS-----|')

    # Montando extrutura de pseudotabela
    for idx in range(0, len(dicionario['CULTURA'])):
        print(f"|{idx:<4} | {dicionario['CULTURA'][idx]:<5} | {dicionario['AREA'][idx]:<12} | {dicionario['INSUMOS'][idx]:<15} |")

#FUNÇÃO DESTINADA CALCULAR A CULTURA
def inserir_dados(): 

    # Declarando variaveis globais
    global area, insumo, manejo_insumo, cultura

    # Tentativa
    try: #<- try é um comando built in do Python cujo ele vai iniciar um bloco de tentantiva de execução do código
        # Input da cultura a ser utilizada
        cultura = input('DIGITE A CULTURA QUE DESEJA INCLUIR:\nMILHO\nSOJA\nR:').upper()

        # MILHO
        if cultura == 'MILHO':
            
            # Aviso
            print('\nA cultura escolhida foi o milho.\nA cultura de milho tem a caracteristica de ser cultivada em uma area quadrada com fertilizante.\nA cada m² serão aplicados 100g de fertilizante.')

            # CALCULE A AREA PLANTADA 
            m = int(input('DIGITE EM METROS O TAMANHO DE UM DOS LADOS DA AREA PARA CALCULAR A AREA EM M²: '))
            area = round(m ** 2, 2)

            # CALCULE O MANEJO DE INSUMOS
            insumo = 100
            manejo_insumo = round(area * insumo,2)

        # SOJA
        elif cultura == 'SOJA':

            # Aviso
            print('\nA cultura escolhida foi o soja.\nA cultura de soja tem a caracteristica de ser cultivada em uma area redonda com fertilizante.\nA cada m² serão pulverizados 500ml de defensivo de soja.')

            # CALCULE A AREA PLANTADA
            r = int(input('DIGITE EM METROS O RAIO DA AREA: '))
            area = round(pi * r ** 2,2)

            # CALCULE O MANEJO DE INSUMOS
            insumo = 500
            manejo_insumo = round(area * insumo,2)

    # Excessao
    except ValueError as error: #<- except faz parte do bloco "try". Aqui é onde indicamos a excessão (erro) que pode iniciar o codigo dentro desse bloco
        print('Algo não ocorreu como deveria.\nTente novamente') #<- Comando presente


while True:
# LIMPEZA DO TERMINAL

    # Apresentação do menu
    print(' '*8,'MENU',' '*8,'\n','-'*22,'\n 1 - Inserir dados\n 2 - Exibir dados\n 3 - Atualizar dados\n 4 - Deletar dados\n 5 - Sair\n','-'*22)
    menu_select = int(input('Qual ação gostaria de executar?\n '))

    # INSERÇÃO DE DADOS
    if menu_select == 1:
        os.system('cls')

         # Declarando variavel de loop
        resp_menu_1 = True
        
        while resp_menu_1 == True:
            inserir_dados()

            # ARMAZENE TUDO EM LISTAS
            dados['CULTURA'].append(cultura)
            dados['AREA'].append(area)
            dados['INSUMOS'].append(manejo_insumo)
            os.system('cls')

            resp_menu_1 = int(input('\nDESEJA INSERIR DADOS\n1-SIM\n2-NAO\nR: '))

    
    # EXIBIÇÃO DE DADOS
    elif menu_select == 2:     
        os.system('cls')   
        exibir_dados(dados)
        
        input('Cados deseje voltar para o Menu aperte qualquer tecla.')
        os.system('cls')
    # ATUALIZAÇÃO DE DADOS
    elif menu_select == 3:
        os.system('cls')

        # Definindo variavel de LOOP
        resp_menu_3 = 1

        # Looping de atualização de dados
        while resp_menu_3 == True:
            exibir_dados(dados)

            # Definindo index que será alterado
            idx = int(input('\nEscolha os dados que deseja alterar: '))

            # Condição para validação de index existente
            if idx > len(dados):
                os.system('cls')
                print(ValueError('O valor escolhido pelo usuário não corresponde a um indice valido.'))
                sleep(1)
                continue

            # Definido novos dados
            inserir_dados()

            # Atualização dos dados da lista
            dados['CULTURA'][idx] = cultura
            dados['AREA'][idx] = area
            dados['INSUMOS'][idx] = manejo_insumo

            resp_menu_3 = int(input('Desja atualizar mais algum dado da tabela?\n1-SIM\n2-NAO\nR: '))

        os.system('cls')

    # EXCLUSÃO DE DADOS
    elif menu_select == 4:
        
        resp_menu_4 = True
        while resp_menu_4 == True:
            exibir_dados(dados)

            # Definindo index que será alterado
            idx = int(input('\nEscolha os dados que deseja excluir da tabela: '))

            # Condição para validação de index existente
            if idx > len(dados):
                os.system('cls')
                print(ValueError('O valor escolhido pelo usuário não corresponde a um indice valido.'))
                sleep(1)

            # Atualização dos dados da lista
            del dados['CULTURA'][idx] 
            del dados['AREA'][idx]
            del dados['INSUMOS'][idx] 

            # Atualização variavel de loop (utilizado para determinar se devemos continuar)
            resp_menu_4 = int(input('Desja atualizar mais algum dado da tabela?\n1-SIM\n2-NAO\nR: '))
        os.system('cls')
    # # EXIT
    elif menu_select == 5:
        exit()



