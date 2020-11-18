### Video = https://www.youtube.com/watch?v=a7DH88vk2Sk

'''Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

Gostou da aula? Então torne-se um Gafanhoto APOIADOR do CursoemVídeo acessando o site cursoemvideo.com/apoie

Aula do Curso de Python criado pelo professor Gustavo Guanabara para o portal CursoemVideo.com.

Curso em Vídeo
Seja um apoiador: http://cursoemvideo.com/apoie
Site: http://www.cursoemvideo.com
YouTube: http://www.youtube.com/cursoemvideo
Facebook: http://www.facebook.com/cursosemvideo
Twitter: http://twitter.com/cursosemvideo
Google+: http://plus.google.com/11266655883741...

Patrocínio
HOSTNET: http://www.hostnet.com.br
GAFANHOTOS: http://apoie.me/cursoemvideo'''

'''Quando queremos fatiar uma lista saltando 2 em 2 veja'''

frase=['Curso em Vídeo Puthon']
#frase[9:21:2]

'''agora iremos aprender a função len'''
# len significa comprimento
# https://www.youtube.com/watch?v=a7DH88vk2Sk
# tempo: 12:00
len(frase)
frase.count('o')

frase.count('o',0,13) #contagem com fatiamento

frase.find('deo') # irá indicar o inicio das letras ao encontrar

frase.find('Androif') #quando não existe ele dirá no resultado -1

'Curso' in frase # ele dirá true

frase.replace('Python','Android') #mode de substituir a lista imutavel

frase.upper() # ira deixar tudo em maiúscula

fase.lower() #deixa tudo em minúsculo

fase.capitalize() #irá jogar todos para minúsculo, mas primeira para maiuscula

fase.title() #conta em palavras

frase = ['  Aprenda Python  ']

frase.strip() # remove os espaços do inicio e do fim

frase.rstrip() # remove somente os ultimos espaços

frase.lstrip() # remove somente os espaços da esquerda

tempo de vido: 26:50 fala sobre Divisão

frase.split() #divide as palavras e refaz os novos indices

'-'.join(frase) # insere nos espaços o ifem



