'''
Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. 
No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. 
Se algum valor for negativo, mostre uma mensagem informando o erro.
'''
import os


atividade_A = int(input('Quantos dias foram necessários para realizar a atividade A? \n'))
atividade_B = int(input('Quantos dias foram necessários para realizar a atividade B? \n'))
atividade_C = int(input('Quantos dias foram necessários para realizar a atividade C? \n'))


def calcula_total(atividade_A, atividade_B, atividade_C):
    if atividade_A < 0 or atividade_B < 0 or atividade_C < 0:
        print('Erro! Não podemos cadastrar números negativos, tente novamente!')
    else: 
        resultado = atividade_A + atividade_B + atividade_C
        print(f'A quantidade de dias gastos foi: {resultado}')

calcula_total(atividade_A, atividade_B, atividade_C)

