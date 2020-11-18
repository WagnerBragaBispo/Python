#https://www.youtube.com/watch?v=K10u3XIf1-Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=38
#tempo: 28:22hs

'''Escreva um programa que leia a velocidade de um carro.'''

'''Se ele ultrapassar 80Km/h, mostre uma menssagem dizendo que ele foi multado'''

'''A multa vai custar R$7,00 por cada km acima do limite'''

vel = int(input('Digite a velocidade do seu carro: '))
lim = 80
cus = 7
dif = vel - lim
dc = dif * cus

if vel >80:
    print('Seu veículo ultrapassou a velocidade permitida de {}km/h em {}km/h. Você será multado hein R${:.2f}!'.format(lim, dif, dc))
else:
    print('Seu veículo está dentro do limite de velocidade. PARABÉNS!')
