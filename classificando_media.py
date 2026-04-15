'''
Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, 
ficaram de recuperação ou reprovados. As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado
Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.
'''

print('BEM VINDO AO COMPUTADOR CALCULA MÉDIA:\n')

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))

def calcula_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    print(f'Sua média é {media:.2f}')
    if media < 5:
        print('Você foi reprovado!')
    elif  5 <=  media < 7:
        print('Você está de recuperação!')
    else:
        print('Você está aprovado!')    

print()
calcula_media(nota1, nota2, nota3)        