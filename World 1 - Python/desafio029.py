print('==== DESAFIO 029 ====')
v = float(input('Qual a velocidade atual do carro? '))
if v <= 80:
    print('Você está dentro do limite (80km/h), muito bem!')
else:
    print('MULTADO! Você está acima do limite, e deverá pagar uma multa de R${:.2f}'.format((v-80) * 7))
print('Dirija com segurança!')
