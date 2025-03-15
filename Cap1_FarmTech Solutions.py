from IPython.display import clear_output
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
def inserir_dados(loop: bool = True): 
    # Declarando variaveis globais
    global area, insumo, manejo_insumo, resp_menu_1, cultura

    try:
        # Declarando variavel de loop
        resp_menu_1 = True

        # Input da cultura a ser utilizada
        cultura = input('DIGITE A CULTURA QUE DESEJA INCLUIR:\nMILHO\nSOJA\nR:').upper()

        while resp_menu_1 == True:

            # MILHO
            if cultura == 'MILHO':
                
                # Aviso
                print('\nA cultura escolhida foir o milho.\nA cultura de milho tem a caracteristica de ser cultivada em uma area quadrada com fertilizante.\nA cada m² serão aplicados 100g de fertilizante.')

                # CALCULE A AREA PLANTADA 
                m = int(input('DIGITE EM METROS O TAMANHO DE UM DOS LADOS DA AREA PARA CALCULAR A AREA EM M²: '))
                area = round(m ** 2, 2)

                # CALCULE O MANEJO DE INSUMOS
                insumo = 100
                manejo_insumo = round(area * insumo,2)

            # SOJA
            elif cultura == 'SOJA':

                # Aviso
                print('\nA cultura escolhida foir o soja.\nA cultura de soja tem a caracteristica de ser cultivada em uma area redonda com fertilizante.\nA cada m² serão pulverizados 500ml de defensivo de soja.')

                # CALCULE A AREA PLANTADA
                r = int(input('DIGITE EM METROS O RAIO DA AREA: '))
                area = pi * r ** 2

                # CALCULE O MANEJO DE INSUMOS
                insumo = 500
                manejo_insumo = round(area * insumo,2)
                

            resp_menu_1 = int(input('\nDESEJA INSERIR DADOS\n1-SIM\n2-NAO\nR: ')) if loop == True else False
    except ValueError as error:
        print('Algo não ocorreu como deveria.\nTente novamente')


while True:
# LIMPEZA DO TERMINAL
    clear_output()    
    print(' '*8,'MENU',' '*8,'\n','-'*22,'\n 1 - Inserir dados\n 2 - Exibir dados\n 3 - Atualizar dados\n 4 - Deletar dados\n 5 - Sair\n','-'*22)
    menu_select = int(input('Qual ação gostaria de executar?\n '))

    # INSERÇÃO DE DADOS
    if menu_select == 1:
        
        inserir_dados()

        # ARMAZENE TUDO EM LISTAS
        dados['CULTURA'].append(cultura)
        dados['AREA'].append(area)
        dados['INSUMOS'].append(manejo_insumo)

    
    # EXIBIÇÃO DE DADOS
    elif menu_select == 2:        
        exibir_dados(dados)

    # ATUALIZAÇÃO DE DADOS
    elif menu_select == 3:

        # Definindo variavel de LOOP
        resp_menu_3 = 1

        # Looping de atualização de dados
        while resp_menu_3 == True:
            exibir_dados(dados)

            # Definindo index que será alterado
            idx = int(input('\nEscolha os dados que deseja alterar: '))

            # Definido novos dados
            inserir_dados(False)

            # Atualização dos dados da lista
            dados['CULTURA'][idx] = cultura
            dados['AREA'][idx] = area
            dados['INSUMOS'][idx] = manejo_insumo

            resp_menu_3 = int(input('Desja atualizar mais algum dado da tabela?\n1-SIM\n2-NAO\nR: '))


    # EXCLUSÃO DE DADOS
    elif menu_select == 4:
        resp_menu_4 = True
        while resp_menu_4 == True:
            exibir_dados(dados)

            # Definindo index que será alterado
            idx = int(input('\nEscolha os dados que deseja excluir da tabela: '))

            # Atualização dos dados da lista
            del dados['CULTURA'][idx] 
            del dados['AREA'][idx]
            del dados['INSUMOS'][idx] 

            # Atualização variavel de loop (utilizado para determinar se devemos continuar)
            resp_menu_3 = int(input('Desja atualizar mais algum dado da tabela?\n1-SIM\n2-NAO\nR: '))

    # # EXIT
    elif menu_select == 5:
        exit()



