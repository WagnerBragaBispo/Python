# https://www.youtube.com/watch?v=a7DH88vk2Sk
# tempo: 31:00

# frase = 'Crurso em Vídeo Python'
#print(frase[::2])

# print('''Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

# Gostou da aula? Então torne-se um Gafanhoto APOIADOR do CursoemVídeo acessando o site cursoemvideo.com/apoie

# Aula do Curso de Python criado pelo professor Gustavo Guanabara para o portal CursoemVideo.com.''')

# print(frase.count('o'))
# print(frase.upper().count('O'))
# print(len(frase))



# frase = '    Currso em Vídeo Python   '
# print(frase.strip())

frase = 'Curso em Vídeo Python'
# frase.replace('Python', 'Android') #neste modo não altera a frase
# frase = frase.replace('Python', 'Android')
# print(frase)
# print('Curso' in frase)
#
# print(frase.find('Vídeo'))
# print(frase.lower().find('vídeo'))
# print(frase.split())

dividido = frase.split() # o split transforma numa lista a frase
# print(dividido)
# print(dividido[0])
print(dividido[2][3])
