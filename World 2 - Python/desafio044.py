print(f'{"IR LOJAS":=^40}')
v = float(input('Valor das compras: R$ '))
print('''Formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
e = int(input('Escolha uma opção: '))
if e == 1:
    print(f'Sua compra de R${v:.2f} vai ser paga com desconto de 10%')
    print(f'No final o valor a ser pago é de R${v * 0.9:.2f}')
elif e == 2:
    print(f'Sua compra de R${v:.2f} vai ser paga com 5% de desconto')
    print(f'No final o valor a ser pago é de R${v * 0.95:.2f}')
elif e == 3:
    print(f'Sua compra de R${v:.2f} vai ser paga em 2x no cartão')
    print(f'O valor das parcelas serão de R${v / 2:.2f}')
elif e == 4:
    p = int(input('Quantas parcelas? '))
    vf = v * 1.2
    print(f'Sua compra de R${v:.2f} vai ser paga em {p} parcelas, com juros de 20%')
    print(f'No final o valor a ser pago é de R${vf:.2f} com parcelas de R${vf / p:.2f}')
else:
    print('Digite uma opção válida!')
    