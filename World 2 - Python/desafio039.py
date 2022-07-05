from datetime import date
nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, ano_atual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}'.format(18 - idade + ano_atual))
elif idade == 18:
    print('Você precisa se alistar esse ano!!!')
else:
    print('Você deveria ter se alistado há {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(ano_atual - (idade - 18)))
