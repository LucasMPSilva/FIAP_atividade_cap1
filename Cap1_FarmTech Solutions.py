from IPython.display import clear_output
from time import sleep
from math import pi


dados = {'CULTURA':['MILHO', 'SOJA', 'SOJA'],
        'AREA':[210201, 520002, 2010203],
        'INSUMOS':[431214, 345344, 546456]}

# MENU
# Boas Vindas
# print('Bem vindo ao aplicativo da FarmTech Solution\n\n')
def exibir_dados(dicionario):
    print('\n|INDEX|CULTURA|--AREA--|--INSUMOS--|')
    for idx in range(0, len(dicionario['CULTURA'])):
        print(f"|{idx:<4} | {dicionario['CULTURA'][idx]:<5} | {dicionario['AREA'][idx]:<5} | {dicionario['INSUMOS'][idx]:<9} |")
# Definindo variavel de looping
while True:
# LIMPEZA DO TERMINAL
    clear_output()    
    print(' '*8,'MENU',' '*8,'\n','-'*22,'\n 1 - Inserir dados\n 2 - Exibir dados\n 3 - Atualizar dados\n 4 - Deletar dados\n 5 - Sair\n','-'*22)
    menu_select = int(input('Qual ação gostaria de executar?\n '))

    # INSERÇÃO DE DADOS
    if menu_select == 1:
        resp = 1
        # LIMPEZA DO TERMINAL
        while resp == 1:
            # ESCOLHA A CULTURA
            clear_output()
            cultura = input('DIGITE A CULTURA QUE DESEJA INCLUIR:\nMILHO\nSOJA\nR:').upper()

                # MILHO
            if cultura == 'MILHO':
                print('\nA cultura escolhida foir o milho.\nA cultura de milho tem a caracteristica de ser cultivada em uma area quadrada com fertilizante.\nA cada m² serão aplicados 100g de fertilizante.')
                    # CALCULE A AREA PLANTADA 
                v_dist = int(input('DIGITE EM METROS O TAMANHO DE UM DOS LADOS DA AREA PARA CALCULAR A AREA EM M²: '))
                area = v_dist ** 2
                    # CALCULE O MANEJO DE INSUMOS
                insumo = 100
                manejo_insumo = round(area * insumo,2)
                    # ARMAZENE TUDO EM LISTAS
                dados['CULTURA'].append(cultura)
                dados['AREA'].append(area)
                dados['INSUMOS'].append(manejo_insumo)
                # lista = lista.update({cultura:[metros,area,manejo_insumo]})
                # print(' CULTURA :   M² | AREA | INSUMO\n',dados)

                # SOJA
            elif cultura == 'SOJA':
                print('\nA cultura escolhida foir o soja.\nA cultura de soja tem a caracteristica de ser cultivada em uma area redonda com fertilizante.\nA cada m² serão pulverizados 500ml de defensivo de soja.')
                    # CALCULE A AREA PLANTADA
                v_dist = int(input('DIGITE EM METROS O RAIO DA AREA: '))
                area = pi * v_dist ** 2

                    # CALCULE O MANEJO DE INSUMOS
                insumo = 500
                manejo_insumo = round(area * insumo,2)

                    # ARMAZENE TUDO EM LISTAS
                dados['CULTURA'].append(cultura)
                dados['AREA'].append(area)
                dados['INSUMOS'].append(manejo_insumo)
                # lista = {cultura:[raio,area,manejo_insumo]}
                # print(' CULTURA : RAIO | AREA | INSUMO\n',lista)

            else:
                print('\nDIGITE UMA CULTURA VALIDA')
            resp = int(input('\nDESEJA INSERIR MAIS DADOS\n1-SIM\n2-NAO\nR: '))
    # EXIBIÇÃO DE DADOS
    elif menu_select == 2:
        exibir_dados(dados)

    # ATUALIZAÇÃO DE DADOS
    # elif menu_select == 3:

    # # EXCLUSÃO DE DADOS
    # elif menu_select == 4:
    # # EXIT
    elif menu_select == 5:
        exit()
