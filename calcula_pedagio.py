'''
Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. 
O valor do pedágio depende da distância percorrida:

Até 100 km: R$ 10,00
Entre 100 km e 200 km: R$ 20,00
Acima de 200 km: R$ 30,00
Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.
'''

print('''                    
██████╗░███████╗██████╗░░█████╗░░██████╗░██╗░█████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝░██║██╔══██╗
██████╔╝█████╗░░██║░░██║███████║██║░░██╗░██║██║░░██║
██╔═══╝░██╔══╝░░██║░░██║██╔══██║██║░░╚██╗██║██║░░██║
██║░░░░░███████╗██████╔╝██║░░██║╚██████╔╝██║╚█████╔╝
╚═╝░░░░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░╚════╝░
''')

distância_percorrida = int(input('''
Você está dirigindo o seu carro e se aproxima de um pedágio...

Funcionário:
Qual a distância percorrida em Km? Exemplo: 100

Sua resposta: 
'''))

def calcula_pedagio(distância_percorrida):
    if distância_percorrida < 100:
        print(f'Funcionário: Como o senhor(a) percorreu {distância_percorrida}km, o valor do pedágio é R$ 10,00')
    elif 100 <= distância_percorrida <= 200:
        print(f'Funcionário: Como o senhor(a) percorreu {distância_percorrida}km, o valor do pedágio é R$ 20,00')
    else:
        print(f'Funcionário: Como o senhor(a) percorreu {distância_percorrida}km, o valor do pedágio é R$ 30,00')

calcula_pedagio(distância_percorrida)