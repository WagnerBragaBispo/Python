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

