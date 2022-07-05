from time import sleep
import random
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
e = int(input('Qual a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('=-' * 15)
pc = random.randint(0, 2)
if pc == 0:
    print('O computador jogou PEDRA')
    if e == 0:
        print('Você jogou PEDRA')
        print('=-' * 15)
        print('EMPATE')
    elif e == 1:
        print('Você jogou PAPEL')
        print('=-' * 15)
        print('Jogador venceu!')
    elif e == 2:
        print('Você jogou TESOURA')
        print('=-' * 15)
        print('Computador venceu!')
    else:
        print('Digite uma opção válida')
elif pc == 1:
    print('O computador jogou PAPEL')
    if e == 0:
        print('Você jogou PEDRA')
        print('=-' * 15)
        print('Computador venceu!')
    elif e == 1:
        print('Você jogou PAPEL')
        print('=-' * 15)
        print('EMPATE')
    elif e == 2:
        print('Você jogou TESOURA')
        print('=-' * 15)
        print('Jogador venceu!')
    else:
        print('Digite uma opção válida')
elif pc == 2:
    print('O computador jogou TESOURA')
    if e == 0:
        print('Você jogou PEDRA')
        print('=-' * 15)
        print('Jogador venceu!')
    elif e == 1:
        print('Você jogou PAPEL')
        print('=-' * 15)
        print('Computador venceu!')
    elif e == 2:
        print('Você jogou TESOURA')
        print('=-' * 15)
        print('EMPATE')
    else:
        print('Digite uma opção válida')
