n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Com a média {:.1f} você está REPROVADO!'.format(m))
    print('Estude mais!')
elif m >= 5 and m <  7:
    print('Com a média {:.1f} você está de RECUPERAÇÃO'.format(m))
    print('Estude mais um pouco e tente novamente!')
elif m >= 7:
    print('Com a média {:.1f} você  está APROVADO!'.format(m))
    print('Parabéns!')
