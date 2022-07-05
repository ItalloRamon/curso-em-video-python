n = int(input('Digite um número para ver seu fatorial: '))
print(f'O fatorial de {n}! é ',end='')
print(n, end='')
f = 1
while n > 0:
    f = f * n
    n += -1
    if n != 0:
        print(f' x {n}',end='')
print(f' = {f}')
    