'''
Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar.
Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. 
Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e 
exiba uma mensagem informando se o acesso é permitido ou negado.
'''

horario_de_entrada = int(input('Digite a hora atual (formato 24 horas): '))

def acesso(horario_de_entrada):
    if 8 <= horario_de_entrada <= 18:
        print('Acesso liberado')
    else:
        print('Acesso negado')

acesso(horario_de_entrada)