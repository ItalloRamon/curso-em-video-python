print('==== DESAFIO 015 ====')
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados com o carro? '))
print('O total a paga de aluguel é R${:.2f}'.format( ((dias * 60) + (km * 0.15)) )) 
