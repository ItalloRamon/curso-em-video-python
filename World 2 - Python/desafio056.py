media = 0
i_velho = 0
n_velho = ''
c = 0
for p in range(1, 5):
    print(f'---- {p}ª PESSOA ----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    media += idade

    if p == 1 and sexo == 'M':
        i_velho = idade
        n_velho = nome 
    elif sexo == 'M':
        if idade > i_velho:
            i_velho = idade
            n_velho = nome
    
    if sexo == 'F':
        if idade < 20:
            c += 1
            
print(f'A média de idade do grupo  é de {media / 4:.1f} anos')
print(f'O homem mais velho tem {i_velho} anos e se chama {n_velho}')
print(f'Ao todo são {c} mulheres com menos de 20 anos')
