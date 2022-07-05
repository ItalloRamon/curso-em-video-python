print('==== DESAFIO 034 ====')
s = float(input('Qual o salário do funcionário: R$ '))
if s > 1250:
    print('O salário agora é {:.2f}'.format(s * 0.1 + s))
else:
    print('O salário agora é {:.2f}'.format(s * 0.15 + s))
print('Parabéns pelo aumento!')