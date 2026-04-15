'''
Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas. 
O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. 
Crie um programa que receba o peso (em kg) e a altura (em metros) e 
calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) 
Depois, exiba o valor do IMC e 
uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).
'''

altura = float(input('Qual sua altura em metros? Exemplo: 1.75\n'))
peso = float(input('Qual seu peso em kg? Exemplo: 75\n'))

def calcula_imc(altura, peso):
    imc = peso / (altura**2)
    print(f'Seu IMC é de: {imc:.2f}')
    if imc < 18.5:
        print('Você está abaixo do peso, o valor do seu IMC é menor do que 18.5.')
    elif 18.5 >=  imc < 25:
        print('Você está com o peso normal, o valor do seu IMC é entre 18.5 e 25.')
    else:
        print('Você está acima do peso, o valor do seu IMC é maior do que 25.')

calcula_imc(altura, peso)