'''
Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:
* O valor da renda mensal precisa ser maior que R$ 2.000,00.
* O valor da parcela não pode ultrapassar 30% da renda.
Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. 
O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.
'''

print('''
███████╗███╗░░░███╗██████╗░██████╗░███████╗░██████╗████████╗██╗███╗░░░███╗░█████╗░
██╔════╝████╗░████║██╔══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝██║████╗░████║██╔══██╗
█████╗░░██╔████╔██║██████╔╝██████╔╝█████╗░░╚█████╗░░░░██║░░░██║██╔████╔██║██║░░██║
██╔══╝░░██║╚██╔╝██║██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░██║██║╚██╔╝██║██║░░██║
███████╗██║░╚═╝░██║██║░░░░░██║░░██║███████╗██████╔╝░░░██║░░░██║██║░╚═╝░██║╚█████╔╝
╚══════╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝░╚════╝░
''')

renda_mensal = int(input('Digite o valor da sua renda mensal em R$:\n'))
valor_parcela = int(input('Digite o valor da parcela desejada R$:\n'))

def  aprova_emprestimo (renda_mensal, valor_parcela):
    if(renda_mensal > 2000 and valor_parcela <= renda_mensal * 0.3 ):
        print('Empréstimo aprovado')
    elif(renda_mensal <= 2000):
        print('Renda mensal insuficiente')
    else:
        print('Valor parcela acima de 30%')

aprova_emprestimo(renda_mensal, valor_parcela)