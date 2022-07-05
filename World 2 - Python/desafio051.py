a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
an = a1 + (10 - 1) * r
for c in range(a1, an + 1, r):
    print(c, end=' > ')
print('Acabou!')