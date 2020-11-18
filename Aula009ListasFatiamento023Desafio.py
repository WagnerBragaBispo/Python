#https://www.youtube.com/watch?v=a7DH88vk2Sk
# tempo: 42:02
# resposta https://www.youtube.com/watch?v=wD2aerLMBWA&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=24
'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados'''

# Ex:
# Digite um número: 1834

# unidade: 4
# dezena: 3
# Centena: 8
# milhar: 1

# frazer numa forma como string ou matematica

######## exemplo de leitura de string com numero
# num = int(input('Digite um número: '))
# n = str(num)
# print('Analisando o número {}'.format(num))
# print('Unidade: {}'.format(n[3]))
# print('Dezena: {}'.format(n[2]))
# print('Centena: {}'.format(n[1]))
# print('Milhar: {}'.format(n[0]))

num = int(input('Digite um número: '))
u = num //1 % 10        # % 10 é o resto da divisao
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))




