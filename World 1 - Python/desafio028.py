from random import randint
from time import sleep
print('==== DESAFIO 028 ====')
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
num = randint(0, 5)
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if n == num:
    print(f'Parabéns, você advinhou! Eu pensei no número {num}')
else:
    print(f':( Infelizmente você não conseguiu advinhar, eu pensei no número {num}')