# https://www.youtube.com/watch?v=a7DH88vk2Sk
#tempo: 40:50

'''Crie um programa que leia o nome completo de uma pessoa e mostre:'''

'''O nome com todas as letras maiúsculas '''

'''O nome com todas mínusculas'''

'''Quantas letras ao todo(sem cosiderar espaços'''

'''Quantas letras tem o primeiro nome'''

nome = input('Digite seu nome completo: ')

print('Seu nome em maiúscula é', nome.strip().upper())
print('Seu nome em minúscula é', nome.strip().lower())
print('Seu nome tem ao todo', len(nome)- nome.count(' '), 'letras')
divido = nome.split()
print('Seu primeiro nome é', divido[0].capitalize(), 'e ele têm ', len(divido[0]), 'letras')



# print(nome.replace(' ','-').count('-'))
# print(nome.strip().capitalize())
# print(len(nome.split()))
# print('-'.join(nome.strip()))

