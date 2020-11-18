####utilizando import para bibliotecas

####Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi

####video disponivel: https://www.youtube.com/watch?v=oOUyhGNib2Q

#### inicio da atividade: 19:40 do video

#### na biblioteca gera número aleatoria entre 0 ate 1
import random
#### exemplo 1: num = random.random()
num = random.randint(1, 10)
print(num)

#### dica: se vc digitar "import" + depois dá um espaço + segure a tecla "crtl+espaço". você vera toda a bibliotecas

#### dica: encontre mais bibliotecas:
#### p1: entra no site python.org > entra no topo do site "PyPI" signifa PI Pacote de Index
#### p2: exemplo baixar emoji > faz a busca no site e digita no Pycharm da seguinte forma
#### p3: clica na palavra emoji > depois na lampada > depois "install pack emoji

import emoji
print(emoji.emojize("Olá, Mundo :earth_americas:", use_aliases=True))

##### dica: tempo do video 25:25 - qdo vc quer ver bibliotecas pre instaladas ou instaladas no seu projeto:
#### p1: segura as teclas Ctrl+Alt+S > vá até o seu projeto > Clica em Project Intrepeter > caso desaj incluir clica no sinal de "+".




