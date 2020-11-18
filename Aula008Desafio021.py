####utilizando import para bibliotecas

####Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi

####video disponivel tempo 30:54: https://www.youtube.com/watch?v=oOUyhGNib2Q
#### Resolução do Exercício: https://www.youtube.com/watch?v=9FiEji_fzvk&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=22



### Desafio 21 - Faça um programa em Python que abra e reproduza o áudio de arquivo mp3
'''         Forma de fazer 1 - importando copiando e colando            '''

#### duas forma:
# 1 copiar o arquivo da area de trabalho e depois clica com botão direito na pasta do projeto e "paste"
# 2 copiar o arquivo e colar na pasta: C:\Users\Wagner\PycharmProjects\GanabaraAula008_UtilizandoModulos

'''dica: para instalar o pygma clica com o botão direto em cima do nome "pygame", espere a lampada aparecer e instala o package'''
import pygame
pygame.init()
'''para chamar/iniciar o que tem o package utilize .init()'''
'''no paygame há uma variedade de coisas inclusive imagens para criar jogos, mas para usar o modulo musica vc utiliza o "mixer"'''
pygame.mixer.music.load('aula008desafio021.mp3')
'''após carregar o arquivo acima colocar o seguinte comando'''
pygame.mixer.music.play()
'''mas será necessário colocar no evento o modo de espera'''
pygame.event.wait()

