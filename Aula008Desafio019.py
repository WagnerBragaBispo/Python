####utilizando import para bibliotecas

####Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi

####video disponivel: https://www.youtube.com/watch?v=oOUyhGNib2Q
#### Resolução do Exercício: https://www.youtube.com/watch?v=_Nk02-mfB5I&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=20

#### inicio da atividade: 29:45 do video

### Desafio 19 - Um professor que sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o escolhido.

'''         exercício 1 - importando todo o metodo random            '''

### import random
### priAluno = str(input('Digite o nome do primeiro aluno: '))
### segAluno = str(input('Digite o nome do segundo aluno: '))
### terAluno = str(input('Digite o nome do terceiro aluno: '))
### quaAluno = str(input('Digite o nome do quarto aluno: '))
### lista = [priAluno, segAluno, terAluno, quaAluno]
### escolhido = random.choice(lista)
### print('O aluno escolhido foi {}'.format(escolhido))


'''         exercício 2 - importando apenas os metodos rndom            '''

from random import choice
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))


