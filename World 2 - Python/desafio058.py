from random import randint
print('Sou o seu computador...')
print('Acabei de pensar em um número inteiro entre 0 e 10')
print('Será que você consegue advinhar? Hahah')
num = randint(0, 10)
print(num)
c = 1
n = int(input('Qual o seu palpite? '))
while n != num:
    if n > num:
        print('Menos... Tente mais uma vez.')
        n = int(input('Qual o seu palpite? '))
    else:
        print('Mais... Tente mais uma vez.')
        n = int(input('Qual o seu palpite? '))
    c += 1
print(f'Eu pensei no número {num}, você acertou com {c} tentativas')
