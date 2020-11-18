####utilizando import para bibliotecas

####Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi

####video disponivel tempo 30:32: https://www.youtube.com/watch?v=oOUyhGNib2Q
#### Resolução do Exercício: https://www.youtube.com/watch?v=OPh0nngbBSY&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=21


### Desafio 20 - Um professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''         Forma de fazer 1 - importando todo o metodo random            '''

#### import random
#### n1 = str(input('Primeiro aluno: '))
#### n2 = str(input('Segundo aluno: '))
#### n3 = str(input('Terceiro aluno: '))
#### n4 = str(input('Quarto aulo: '))
#### lista = [n1, n2, n3, n4]
#### random.shuffle(lista)
'''Shuffle significa embaralhar a lista'''
#### print(' A ordem de apresentação será: ')
#### print(lista)

'''         Forma de fazer 2 - utilizando apenas um método deixando o pragrama mais rápido            '''

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aulo: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
'''neste método não precisa utilizar random.shuffle'''
print(' A ordem de apresentação será: ')
print(lista)
