#print(f'"{234:b}"')
n = int(input('Digite um número inteiro: '))
print('Esoclha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HExADECIMAL')
e = int(input('Sua opção: '))
if e == 1:
    #print('{0} convertido para BINÁRIO é igual a {0:b}'.format(n, n))
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif e == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif e  == 3:
    print('{} convertido para HExADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Digite uma opção válida!')

