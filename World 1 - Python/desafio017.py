from math import hypot
print('==== DESAFIO 017 ====')
co = float(input('Qual o comprimento do Cateto Oposto? '))
ca = float(input('Qual o comprimento do Cateto Adjacente? '))
print('Com essas medidas, a hipotenusa desse triângulo mede {:.2f}'.format(hypot(co, ca)))