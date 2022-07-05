n1 = int(input('Primeiro segmneto: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 != n2 and n1 !=  n3 and n2 != n3:
        print('Os segmentos podem formar um TRIÂNGULO ESCALENO')
    elif n1 == n2 and n1 == n3:
        print('Os segmentos podem formar um TRIÂNGULO EQUILÁTERO')
    else:
        print('Os segmentos podem formar um TRIÂNGULO ISÓCELES')
else:
    print('Os segmentos NÃO podem formar um triângulo!')