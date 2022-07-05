print('==== DESAFIO 031 ====')
n = float(input('Qual a distância da sua viagem? KM '))
if n <= 200:
    print('Sua viagem vai custar R${:.2f}'.format(n * 0.5))
else:
    print('Sua viagem vai custar R${:.2f}'.format(n * 0.45))
print('Tenha uma boa viagem!')