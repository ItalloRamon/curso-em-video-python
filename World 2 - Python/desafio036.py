casa = float(input('Valor da casa: R$ '))
s = float(input('Salário do comprador: R$ '))
f = int(input('Quantos anos de financiamento? '))
prestacao = casa / (f * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, f, prestacao))
if prestacao > (s * 0.3):
    print('Empréstimo negado!')
else:
    print('Empréstimo pode ser concedido!')
