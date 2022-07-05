from math import cos, sin, tan, radians
print('==== DESAFIO 018 ====')
ang = float(input('Informe um ângulo: '))
print('O cosseno de {} é {:.2f}'.format(ang, cos(radians(ang))))
print('O seno de {} é {:.2f}'.format(ang, sin(radians(ang))))
print('A tangente de {} é {:.2f}'.format(ang, tan(radians(ang))))
