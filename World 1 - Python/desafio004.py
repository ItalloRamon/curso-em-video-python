print('==== DESAFIO 004 ====')
var = input('Digite algo: ')
print('{} é do tipo {}'.format(var, type(var)))
print('Só tem espaços? {}'.format(var.isspace()))
print('É numérico? {}'.format(var.isnumeric()))
print('É alfabético? {}'.format(var.isalpha()))
print('É alfanumérico? {}'.format(var.isalnum()))
print('Está em maiúsculas? {}'.format(var.isupper()))
print('Está em minúsculas? {}'.format(var.islower()))
print('Está capitalizada? {}'.format(var.istitle()))