print('----------------')
print(' LOJA BARATÃO')
print('----------------')
r = 's'
total = c = barato = contador =  0
while r in 'Ss':
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    r = input('Quer continuar? [S/N] ').strip().upper()[0]
    contador += 1
    
    if contador == 1 or preco < barato:
        barato = preco
        nome_barato = nome

    total += preco
    if preco > 1000:
        c += 1
print('FIM DO PROGRAMA')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {c} produtos que custam mais que R$1000')
print(f'O produto mais barato foi {nome_barato} que custa R${barato:.2f}')
