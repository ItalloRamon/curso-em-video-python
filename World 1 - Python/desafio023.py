print('==== DESAFIO 023 ==== ')
n = int(input('Digite um número: '))
print(f'Analisando o número {n}')
#Meu jeito
print(f'Milhar: {(n % 10000) // 1000}')
print(f'Centena: {(n % 1000) // 100}')
print(f'Dezena: {(n % 100) // 10}')
print(f'Unidade: {n % 10}')

#Solução
#print(f'Milhar: {n // 1000 % 10}')
#print(f'Centena: {n // 100 % 10}')
#print(f'Dezena: {n // 10 % 10}')
#print(f'Unidade: {n // 1 % 10}')
