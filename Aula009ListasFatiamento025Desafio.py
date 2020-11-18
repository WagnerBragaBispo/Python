# https://www.youtube.com/watch?v=a7DH88vk2Sk
# tempo: 43:01
# respota está: https://www.youtube.com/watch?v=WHWGz2Dy1ZU

'''Crie um programa que leia o nome de uma pessoa e dia se ela tem 'Silva' no nome '''

# deve mostrar se tem silva em qualquer parte do nome true ou false

nome = str(input('Qual é o seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
