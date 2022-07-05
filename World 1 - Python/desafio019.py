from random import choice
print('==== DESAFIO 019 ====')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
s = choice([a1, a2, a3, a4])
print('O aluno selecionado foi {}'.format(s))