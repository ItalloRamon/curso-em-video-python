'''n1 = float(input('Peso da 1ª pessoa: '))
n2 = float(input('Peso da 2ª pessoa: '))
n3 = float(input('Peso da 3ª pessoa: '))
n4 = float(input('Peso da 4ª pessoa: '))
n5 = float(input('Peso da 5ª pessoa: '))
list = [n1, n2, n3, n4, n5]
print(f'O maior peso lido foi {max(list):.1f}Kg')
print(f'O menor peso lido foi {min(list):.1f}Kg')
'''

maior = 0
menor = 0
for p in range(1, 6):
    n = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f'O maior peso lido foi {maior}Kg')
print(f'O menor peso lido foi {menor}Kg')