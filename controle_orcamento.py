'''
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. 
O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
'''

orcamento = 3000
despesas = int(input('Digite o total das despesas do mês (R$):\n'))

def controle_de_orcamento(orcamento, despesas):
    resultado = orcamento - despesas
    if resultado < 0:
        print('Atenção! Você ultrapassou o limite do orçamento!')
    else:
        print(f'Você ainda não ultrapassou o limite do orçamento!\n Lhe sobram R${resultado}')

controle_de_orcamento(orcamento, despesas)