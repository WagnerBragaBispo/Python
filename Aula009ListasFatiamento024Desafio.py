# https://www.youtube.com/watch?v=a7DH88vk2Sk
# resposta: https://www.youtube.com/watch?v=QroT8cZMRnc
# tempo 42:32
'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo'''

# pessoa deve digitar o nome da cidade e responde se é santos

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

