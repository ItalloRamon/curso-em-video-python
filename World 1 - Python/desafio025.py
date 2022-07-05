print('==== DESAFIO 025 ====')
n = str(input('Digite seu nome completo: ')).strip().upper()
n1 = n.split()
r = 'SILVA' in n1
print(f'Seu nome tem Silva? {r}')