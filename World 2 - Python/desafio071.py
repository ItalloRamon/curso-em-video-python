valor = int(input('Qual valor será sacado? R$ '))
if valor >= 50:
    n_50 = valor // 50
    print(f'Total de {n_50} cédulas de R$50')
    if (valor % 50) >= 20: 
        n_20 = (valor % 50) // 20
        print(f'Total de {n_20} cédulas de R$20')
        if ((valor % 50) % 20) >= 10:
            n_10 = ((valor % 50) % 20) // 10
            print(f'Total de {n_10} cédulas de R$10')
            if (((valor % 50) % 20) % 10) >= 1:
                n_1 = (((valor % 50) % 20) % 10) / 1
                print(f'Total de {int(n_1)} cédulas de R$1')
        else:
            if (((valor % 50) % 20) % 10) >= 1:
                n_1 = (((valor % 50) % 20) % 10) / 1
                print(f'Total de {int(n_1)} cédulas de R$1')

    if (valor % 50) >= 10 and (valor % 50) < 20:
        n_10 = (valor % 50) // 10
        print(f'Total de {n_10} cédulas de R$10')
        if ((valor % 50) % 10) >= 1:
            n_1 = ((valor % 50) % 10) / 1
            print(f'Total de {int(n_1)} cédulas de R$1')
    if (valor % 50) >= 1 and (valor % 50) < 10:
        n_1 = (valor % 50) / 1
        print(f'Total de {int(n_1)} cédulas de R$1')

if 50 > valor >= 20:
    n_20 = valor // 20
    print(f'Total de {n_20} cédulas de R$20')
    if (valor % 20) >= 10:
        n_10 = (valor % 20) // 10
        print(f'Total de {n_10} cédulas de R$10')
        if ((valor % 20) % 10) >= 1:
            n_1 = ((valor % 20) % 10) / 1
            print(f'Total de {int(n_1)} cédulas de R$1')
    
    if 10 > (valor % 20) >= 1:
        n_1 = (valor % 20) / 1
        print(f'Total de {int(n_1)} cédulas de R$1')

if 20 > valor >= 10:
    n_10 = valor // 10
    print(f'Total de {n_10} cédulas de R$10') 
    if (valor % 10) >= 1:
        n_1 = (valor % 10) / 1
        print(f'Total de {int(n_1)} cédulas de R$1')

if valor < 10:
    n_1 = valor / 1
    print(f'Total de {int(n_1)} cédulas de R$1')
