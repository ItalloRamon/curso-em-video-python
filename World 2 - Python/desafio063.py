print('-' * 20)
print('Sequência Fibonacci')
print('-' * 20)
n = int(input('Quantos termos você quer mostrar? '))
c = 0
f = 0
n1 = 0
n2 = 1
while c < n:
    print(f'{f} > ', end='')
    c += 1
    if f == 1:
        while c < n:
            print(f'{n1 + n2} > ', end='')
            x = n1 + n2
            n1 = n2
            n2 = x
            c += 1
    f += 1
print('FIM')
