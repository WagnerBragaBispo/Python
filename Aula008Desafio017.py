####utilizando import para bibliotecas

####Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi

####video disponivel: https://www.youtube.com/watch?v=oOUyhGNib2Q

#### inicio da atividade: 27:55 do video

### Desafio 17 - Faça um programa que leia o cumprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

'''a resolução do exercício video: https://www.youtube.com/watch?v=vmPW9iWsYkY&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=18'''

'''             exemplo 1 - calculo matemático           '''
#### co = float(input('Comprimwento do cateto oposto: '))
#### ca = float(input('Cumprimento do cateto adjacente: '))
#### hi = (co ** 2 + ca ** 2) ** (1/2)
#### print('A hipotenusa vai medir {:.2f}'.format(hi))

'''             exemplo 2 - importando o metodo math          '''
#### import math
#### co = float(input('Comprimwento do cateto oposto: '))
#### ca = float(input('Cumprimento do cateto adjacente: '))
#### hi = math.hypot(co, ca)
#### print('A hipotenusa vai medir {:.2f}'.format(hi))

'''             exemplo 3 - importando apenas o metodo hypot          '''
from math import hypot
co = float(input('Comprimwento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

