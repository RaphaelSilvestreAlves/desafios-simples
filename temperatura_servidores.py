'''Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. 
Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.
'''

temperatura = int(input('Qual a temperatura atual da sala de servidores?\n'))

if temperatura > 25: print('Alerta! Temperatura acima do limite permitido!')