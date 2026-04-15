'''
Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar. 
Essa verificação será usada para definir ações diferentes dentro do jogo. 
Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar.
'''

print('''
██╗░░░██╗███████╗██████╗░██╗███████╗██╗░█████╗░░█████╗░
██║░░░██║██╔════╝██╔══██╗██║██╔════╝██║██╔══██╗██╔══██╗
╚██╗░██╔╝█████╗░░██████╔╝██║█████╗░░██║██║░░╚═╝███████║
░╚████╔╝░██╔══╝░░██╔══██╗██║██╔══╝░░██║██║░░██╗██╔══██║
░░╚██╔╝░░███████╗██║░░██║██║██║░░░░░██║╚█████╔╝██║░░██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝

██████╗░░█████╗░██████╗░██╗██████╗░░█████╗░██████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝███████║██████╔╝██║██║░░██║███████║██║░░██║█████╗░░
██╔═══╝░██╔══██║██╔══██╗██║██║░░██║██╔══██║██║░░██║██╔══╝░░
██║░░░░░██║░░██║██║░░██║██║██████╔╝██║░░██║██████╔╝███████╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝
''')


numero = int(input('Digite um número inteiro: '))

def paridade(numero):
    if numero % 2 != 0: 
        print(f'O número {numero} é ímpar')
    else:
        print(f'O número {numero} é par')

paridade(numero)