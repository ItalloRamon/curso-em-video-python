n = int(input('Digite um número: '))
s = 0
for c in range(1, n+1):
    if (n % c) == 0:
        print('\033[33m', end = '')
        s += 1
    else:
        print('\033[31m', end = '')
    print(c, end = ' ')
print(f'\n\033[mO número {n} foi divisível {s} vezes')
if s == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')
