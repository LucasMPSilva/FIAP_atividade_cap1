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
def inserir_dados(): 
    # Declarando variaveis globais
    global area, insumo, manejo_insumo, resp, cultura

    # Declarando variavel de loop
    resp = 1

    # Input da cultura a ser utilizada
    cultura = input('DIGITE A CULTURA QUE DESEJA INCLUIR:\nMILHO\nSOJA\nR:').upper()

    while resp == 1:

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

                
        
        else:
            print('\nDIGITE UMA CULTURA VALIDA')

        resp = int(input('\nDESEJA INSERIR MAIS DADOS\n1-SIM\n2-NAO\nR: '))

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
        idx = int(input('Escolha os dados que deseja alterar: '))
        inserir_dados()

        dados['CULTURA'][idx].append(cultura)
        dados['AREA'][idx].append(area)
        dados['INSUMOS'][idx].append(manejo_insumo)

    # # EXCLUSÃO DE DADOS
    # elif menu_select == 4:
    # # EXIT
    elif menu_select == 5:
        exit()



