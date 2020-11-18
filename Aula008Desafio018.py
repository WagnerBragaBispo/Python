####utilizando import para bibliotecas

####Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi

####video disponivel: https://www.youtube.com/watch?v=oOUyhGNib2Q

#### inicio da atividade: 28:41 do video

### Desafio 18 - Faça um programa que leia o angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

### resolução do exercicío no video: https://www.youtube.com/watch?v=9GvsphwW26k&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=19

'''         Exercício 1 - importando toda a biblioteca do metodo math          '''
#### import math
#### ângulo = float(input('Digite o ângulo que você deseja: '))
'''necessário converter para radianos no site do python > docs > indice 9.3 trigonometria'''
#### seno = math.sin(math.radians(ângulo))
#### print('O ângulo de {} tem SENO de {:.2f}'.format(ângulo, seno))
#### cosseno = math.cos(math.radians(ângulo))
#### print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
#### tangente = math.tan(math.radians(ângulo))
#### print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))

'''         Exercício 2 - importando apenas os metodos do math daí retiramos a referencia ".math"         '''
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))
