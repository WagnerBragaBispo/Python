 # Python Comandos


####Python 3.6.4 documentation
https://docs.python.org/3.6/index.html


####The Python Tutorial
https://docs.python.org/3.6/tutorial/index.html

####Para baixar o Python no Linux Ubunto
digite sudo apt-get install python3.6


# ---=========================================================================================================================
# Aula 04 > 
# ---=========================================================================================================================

nome = input('Qual é o seu nome?')
print('Olá',nome,'! Prazer em te conhecer')

dia = input('Digiti o dia do seu nascimento')
mes = input('Digiti o mês do seu nascimento')
ano = input('Digiti o ano do seu nascimento')
print('Você nasceu no dia',dia,'de',mes,'de',ano,'Correto!')

num1=int(input('Primeiro numero'))
num2=int(input('Primeiro numero'))
print(num1+num2)



# ---=========================================================================================================================
# Aula 06a > 
# ---=========================================================================================================================
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma vale', s)

# print('A soma entre ', str(n1), 'e',str(n2), 'igual a ', s)
print('A soma entr {} e {} vale {}'.forma)

# ---=========================================================================================================================
# Aula 07 > Operadores aritiméticos
# ---=========================================================================================================================

#### curso Guanabara aula 07: https://www.youtube.com/watch?v=Vw6gLypRKmY
###os peradores sao categorizados da seguinte forma:
#### + adicao
#### - subtracao
#### * multiplicacao
#### / divisao
#### ** potencia
#### // divisao inteira
#### % resto da divisao

#### no python qdo queremos testar dois operadores eh utilizado dois sinais de iguais

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 + n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))

#### Dica: qdo você deseja que a divisão venha com menos casas decimais. Digitamos {:3f} o "f" significa flutuante.
#### Dica: no print para não que não pule a linha no print devemos incluir no final do código o seguinte comando: ", end='')"
#### Dica: diferente da dica anterior, qdo quero quebrar a linha digitamos no meio do comando: " \n "

# ---=========================================================================================================================
# Aula 07 > Desafio 005
# ---=========================================================================================================================

#### desafio aula 007 desafio 005: https://www.youtube.com/watch?v=Vw6gLypRKmY
#### iniciado no video 31:10
#### soluções dos desafio: https://youtu.be/Vw6gLypRKmY
#### desafio 005: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número inteiro: '))
s = n1 + 1
sub = n1 - 1
print('O número que você digitou é {} e o seu sucessor é {} e o antecessor é {}'.format(n1, s, sub))

# ---=========================================================================================================================
# Aula 07 > Desafio 006
# ---=========================================================================================================================
#### desafio aula 007 desafio 005: https://www.youtube.com/watch?v=Vw6gLypRKmY
#### iniciado no video 31:47
#### desafio 006: Crie um algoritmo que leia um número e monstre o seu dobro, triplo e raiz quadra.
n1 = int(input('Digite um valor: '))
m = n1 * 2
raiz = n1 * n1
print('O número que você criou é {}, \n o seu dobro é {} e a \n raiz quadrada é {}'.format(n1, m, raiz))

# ---=========================================================================================================================
# Aula 07 > Desafio 007
# ---=========================================================================================================================
#### desafio aula 007 desafio 005: https://www.youtube.com/watch?v=Vw6gLypRKmY
#### iniciado no video 32:06
#### desafio 007: Desenvolva um programa que leia as duas notas de um aluno, calcula e mostre suma média
n1 = int(input('Digite a sua primeira nota: '))
n2 = int(input('Digite a sua segunda nota: '))
media_nota = (n1 + n2)/2
print('Como na primeira prova você tirou {} \n e na segunda prova você tirou {} \n sua média é {:.02f}'.format(n1, n2, media_nota))

# ---=========================================================================================================================
# Aula 07 > Desafio 008
# ---=========================================================================================================================
#### desafio aula 007 desafio 005: https://www.youtube.com/watch?v=Vw6gLypRKmY
#### iniciado no video 40:23
#### desafio 008: Escreva um programa que leia um valor em metros e o exiba convertido em centimetros a milimetros.
n1 = int(input('Digite um número em metros:'))
n2 = n1 * 100
n3 = n1 * 1000
print('Os {} metros, equivale a {} centimetros ou {} milímetros .'.format(n1, n2, n3))



# ---=========================================================================================================================
# Cadeia de caracteres ou strings > manipulando texto
# ---=========================================================================================================================
frase=['Curso em Vídeo Puthon']
#frase[9:21:2]

# '''agora iremos aprender a função len'''
# len significa comprimento
# https://www.youtube.com/watch?v=a7DH88vk2Sk

# tempo: 12:00

#-----------fatiamento
frase[9]   		#identificar o caracter 9 partindo do 0 zero
frase[9:13]  	#começa do 9 até o 13, mas ele para de contar a letra 13
frase[9:21:2]	# começa no 9 e vai até o 21 e depois pula 2 em 2 cada caracter
frase[:5]		#Começa do caracter inicial até o caract 5
frase[15:]		# começa do caracter 15 e vai até o final
frase[9::3]		#começa no caracter 9 e vai até o final e depois pula 3 em 3

#-----------analise
len(frase)		#conta qtos caracteres tem frase
frase.count('o') #conta qtos a letras "o" minusculos
frase.count('o',0,13) #contagem com fatiamento
frase.find('deo') # irá indicar o inicio das letras ao encontrar
frase.find('Androif') #quando não existe ele dirá no resultado -1
'Curso' in frase # ele diz se existe a palavra 'curso' dirá true

#-----------transformação
frase.replace('Python','Android') #mode de substituir a lista imutavel
frase.upper() 	# ira deixar tudo em maiúscula
fase.lower() 	#deixa tudo em minúsculo
fase.capitalize() #irá jogar todos para minúsculo, mas primeira para maiuscula
fase.title() 	#coloca o inicio de palavra com a letra maiuscula
frase = ['  Aprenda Python  ']
frase.strip() 	# remove os espaços do inicio e do fim
frase.rstrip() 	# remove somente os ultimos espaços
frase.lstrip() 	# remove somente os espaços da esquerda
frase.split() 	#divide as palavras e refaz os novos indices

'-'.join(frase) # insere nos espaços o ifem

#-----------exemplos
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))

frase = '    Currso em Vídeo Python   '
print(frase.strip())

frase = 'Curso em Vídeo Python'
frase.replace('Python', 'Android') #neste modo não altera a frase
frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)

print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())

dividido = frase.split() # o split transforma numa lista a frase
print(dividido)
print(dividido[0])
print(dividido[2][3])		#montra a 3 letra da palavra 3 pq 0 tb conta

frase = 'Crurso em Vídeo Python'
print(frase[::2])

print('''Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().''')


# ---=========================================================================================================================
# Aula 9 > Desafio 022 caracteres ou strings > manipulando texto
# ---=========================================================================================================================

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


# ---=========================================================================================================================
# Aula 9 > Desafio 023 caracteres ou strings > manipulando texto
# ---=========================================================================================================================

# https://www.youtube.com/watch?v=a7DH88vk2Sk
# tempo: 42:02
# resposta https://www.youtube.com/watch?v=wD2aerLMBWA&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=24
'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados'''

# Ex:
# Digite um número: 1834

# unidade: 4
# dezena: 3
# Centena: 8
# milhar: 1

# frazer numa forma como string ou matematica

######## exemplo de leitura de string com numero
# num = int(input('Digite um número: '))
# n = str(num)
# print('Analisando o número {}'.format(num))
# print('Unidade: {}'.format(n[3]))
# print('Dezena: {}'.format(n[2]))
# print('Centena: {}'.format(n[1]))
# print('Milhar: {}'.format(n[0]))

num = int(input('Digite um número: '))
u = num //1 % 10        # % 10 é o resto da divisao
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))



# ---=========================================================================================================================
# Aula 9 > Desafio 024 caracteres ou strings > manipulando texto
# ---=========================================================================================================================
# https://www.youtube.com/watch?v=a7DH88vk2Sk
# resposta: https://www.youtube.com/watch?v=QroT8cZMRnc
# tempo 42:32
'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo'''
# pessoa deve digitar o nome da cidade e responde se é santos

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')


# ---=========================================================================================================================
# Aula 9 > Desafio 25 caracteres ou strings > manipulando texto
# ---=========================================================================================================================
# https://www.youtube.com/watch?v=a7DH88vk2Sk
# tempo: 43:01
# respota está: https://www.youtube.com/watch?v=WHWGz2Dy1ZU

'''Crie um programa que leia o nome de uma pessoa e dia se ela tem 'Silva' no nome '''

# deve mostrar se tem silva em qualquer parte do nome true ou false

nome = str(input('Qual é o seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))




# ---=========================================================================================================================
# Aula 9 > Desafio 26 caracteres ou strings > manipulando texto
# ---=========================================================================================================================

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


# ---=========================================================================================================================
# Aula 9 > Desafio 27 caracteres ou strings > manipulando texto
# ---=========================================================================================================================
#https://www.youtube.com/watch?v=a7DH88vk2Sk
#tempo: 43:56
# Resposta: https://www.youtube.com/watch?v=SifYYsXhLM8


'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente'''

# Ex: Ana Maria de Souza
# primeira = Ana
# último = Souza

nm = str(input('Digite seu nome completo: ')).upper().strip()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nm.split()[0]).title())
print('Seu último nome é {}'.format(nm.split()[-1]).title())

#forma que o Guanabara ensinou
nome = nm.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))


# ---=========================================================================================================================
# Aula 10 > Condições Parte 01 > manipulando texto
# ---=========================================================================================================================
#https://www.youtube.com/watch?v=K10u3XIf1-Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=38
#tempo: 22:00
# Resposta: 

# Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.
# Veja como aplicar os comandos if: e else: no Python.

nome = str(input('Qual é o seu nome? ')).upper().strip()
if nome == 'WAGNER':
    print('Que nome lindo você têm!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome).title())


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi é {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

# o mesmo exemplo acima, mas de uma forma simplificada
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi de {:.1f}'.format(m))
print('PARABENS!' if m >= 6 else 'ESTUDE MAIS')

# ---=========================================================================================================================
# Aula 10 > Desafio 028 
# ---=========================================================================================================================
#https://www.youtube.com/watch?v=K10u3XIf1-Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=38
#tempo: 27:40
# Resposta: https://www.youtube.com/watch?v=kchC5KLZSZ4&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=39&pbjreload=10

'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador /n O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
computador = randint(0, 5) # Faz o computador "Pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que númerop eu pensei? ')).strip() # Jogador tenta adivinhar
if jogador == computador:
	print('PARABÉNS! Você conseguiu me vencer!')
else:
	print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
	

# ---=========================================================================================================================
# Aula 10 > Desafio 029 
# ---=========================================================================================================================



