n = int(input('Digite um número: '))
resp = str(input('Quer continuar? [S/N] ')).upper().strip()
maior = menor = soma = n
cont = 1
while resp == 'S':
    cont += 1
    n = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma += n
print(f'Você digitou {cont} números e a média foi {soma/cont}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
