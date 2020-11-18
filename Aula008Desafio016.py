####utilizando import para bibliotecas

####Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi

####video disponivel: https://www.youtube.com/watch?v=oOUyhGNib2Q

#### inicio da atividade: 27:45 do video

### Desafio 16 - Crie um programa que leia um número real qualquer pelo teclado e mostre na sua tela a porção inteita.

#### resolução do exercício : https://www.youtube.com/watch?v=-iSbDpl5Jhw&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=18&t=0s


#### ----------------------------------------
####                exemplo 1
#### ----------------------------------------
### import math
### num = float(input('Digite um valor: '))
### print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

#### ----------------------------------------
####                exemplo 2
#### ----------------------------------------
#### from math import trunc
#### num = float(input('Digite um valor: '))
#### print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

#### ----------------------------------------
####                exemplo 3
#### ----------------------------------------
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))
