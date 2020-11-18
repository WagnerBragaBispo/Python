# https://www.youtube.com/watch?v=a7DH88vk2Sk
# resposta: https://www.youtube.com/watch?v=23UOVEetNPY
# tempo: 43:28

'''Faça um programa que leia uma frase pelo teclado e mostre '''

# Quantas vezes aparece a letra 'a'

# Em que posição ela aparece a primeira vez

# Em que posição ela aparece a última vez

# faz o usuário digitar a frase

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aprece {} vezes na fase. '.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'. format(frase.rfind('A')+1))

