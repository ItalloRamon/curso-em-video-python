from  datetime import date
print('==== DESAFIO 032 ====')
n = int(input('Qual ano você quer analisar? Digite 0 para o ano atual: '))
if n == 0:
    n = date.today().year
if (n % 4) == 0: #É divisível por 4? Se sim...
    if (n % 100) != 0: #NÃO é divisível por 100? Então:
        print(f'O ano de {n} é bissexto')
    else: #É divisível por 100? Então: 
        if (n % 400) == 0: #É divisível por 400? Então:
            print(f'O ano de {n} é bissexto')
        else:
            print(f'O ano de {n} não é bissexto')
else:
    print(f'O ano de {n} não é bissexto')
