print('==== DESAFIO 027 ====')
n = str(input('Digite seu nome completo: ')).strip().split()

#Outra solução
#espf = n.rfind(' ') + 1
#espi = n.find(' ')
#print(f'Seu primeiro nome é {n[:espi]}')
#print(f'Seu último nome é {n[espf:]}')


print('Muito prazer em te conhecer')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[len(n) - 1]}')