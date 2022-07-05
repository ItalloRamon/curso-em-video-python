from datetime import date
ano = date.today().year
i = 1
h = 0
l = 0
for c in range(0, 7):
    n = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    if (ano - n) >= 18:
        h += 1
    else:
        l += 1
    i += 1
print(f'Ao todo tivemos {h} pessoas maiores de idade')
print(f'Ao todo tivemos {l} pessoas menores de idade')
