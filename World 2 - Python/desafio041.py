from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificação: MIRIM')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL')
elif 14 < idade <= 19:
    print('Classificação: JÚNIOR') 
elif 19 < idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')
    