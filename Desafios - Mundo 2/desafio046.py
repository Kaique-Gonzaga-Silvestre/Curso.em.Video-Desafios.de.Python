# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre elas. 

from time import sleep

input('APERTE [ ENTER ] PARA COMEÇAR A CONTAGEM PARA O ESTOURO DOS FOGOS DE ARTIFÍCIO  ')

for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('KABOOOOOOOOOOOOOOOOM, OS FOGOS EXPLODIRAM')
