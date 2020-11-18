#https://www.youtube.com/watch?v=a7DH88vk2Sk
#tempo: 43:56
# Resposta: https://www.youtube.com/watch?v=SifYYsXhLM8


'''Faça um programa que leia o nome completo de uma pesprisoa, mostrando em seguida o primeiro e o último nome separadamente'''

# Ex: Ana Maria de Souza
# primeira = Ana
# último = Souza

nm = str(input('Digite seu nome completo: ')).upper().strip()
print('Muito prazer em te conhecer!')
#print('Seu primeiro nome é {}'.format(nm.split()[0]).title())
#print('Seu último nome é {}'.format(nm.split()[-1]).title())

#forma que o Guanabara ensinou
nome = nm.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

