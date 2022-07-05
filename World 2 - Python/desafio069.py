total18 = totalsexom = totalsexof = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    if idade > 18:
        total18 += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        totalsexom += 1
    elif sexo == 'F' and idade < 20:
        totalsexof += 1
    print('-' * 20)
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'TOTAL DE PESSOAS COM MAIS DE 18 ANOS: {total18}')
print(f'TOTAL DE HOMENS CADASTRADOS: {totalsexom}')
print(f'TOTAL DE {totalsexof} MULHERES COM MENOS DE 20 ANOS')
