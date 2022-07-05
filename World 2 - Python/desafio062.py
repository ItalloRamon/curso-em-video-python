a1 = int(input('Primeiro termo: '))
r= int(input('Razão: '))
c = 1
while c <= 10:
    print(f'{a1} > ', end='')
    a1 += r
    c += 1
print('PAUSA')
opcao = int(input('Quantos termos quer mostrar a mais? '))
v = opcao + 10
while opcao != 0:
    while c <= v:
        print(f'{a1} > ', end='')
        a1 += r
        c += 1
    print('PAUSA')
    opcao = int(input('Quantos termos quer mostrar a mais? '))
    v += opcao
print(f'Progressão finalizada com {c-1} termos mostrados!')
