a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
while c <= 10:
    print(f'{a1} > ', end='')
    a1 += r
    c += 1
print('Fim')
