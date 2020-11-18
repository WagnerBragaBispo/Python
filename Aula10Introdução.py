#nome = str(input('Qual é o seu nome? ')).upper().strip()
#if nome == 'WAGNER':
#    print('Que nome lindo você têm!')
#else:
#    print('Seu nome é tão normal!')
#print('Bom dia, {}'.format(nome).title())


#novo exemplo

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# m = (n1 + n2)/2
# print('Sua média foi é {:.1f}'.format(m))
# if m >= 6.0:
#    print('Sua média foi boa! PARABÉNS!')
# else:
#    print('Sua média foi ruim! ESTUDE MAIS!')

# o mesmo exemplo acima, mas de uma forma simplificada
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi de {:.1f}'.format(m))
print('PARABENS!' if m >= 6 else 'ESTUDE MAIS')
