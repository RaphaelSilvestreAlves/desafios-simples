'''
Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. 
Ele registrou a quantidade vendida de dois produtos: maçãs e bananas.
Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. 
Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
'''

macas_vendidas = int(input('Digite quantas maçãs foram vendidas: \n'))
bananas_vendidas = int(input('Digite quantas bananas foram vendidas: \n'))


def calcula_vendas(macas_vendidas, bananas_vendidas):
    if macas_vendidas > bananas_vendidas:
        resultado = macas_vendidas - bananas_vendidas
        print(f'As maçãs tiveram mais vendas.\nForam vendidas {resultado} maçãs a mais do que bananas')
    elif macas_vendidas == bananas_vendidas:
        print(f'As maçãs e as bananas tiveram a mesma quantidade de vendas.\nForam vendidas {macas_vendidas} maçãs e {bananas_vendidas} bananas')
    else:
        resultado = bananas_vendidas - macas_vendidas
        print(f'As bananas tiveram mais vendas.\nForam vendidas {resultado} bananas a mais do que maçãs')

calcula_vendas(macas_vendidas, bananas_vendidas)