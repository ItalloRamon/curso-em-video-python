print('==== DESAFIO 022 ====')
nome = str(input('Digite seu nome completo: ')).strip()
espacos = nome.count(' ')
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - espacos} letras')
first = nome.split()
print(f'Seu primeiro nome é {first[0]} e ele tem {len(first[0])} letras')