from random import randint
print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)
vitoria = 0
while True:
    n = int(input('Diga um valor: '))
    escolha = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    pc = randint(0, 100)
    s = n + pc
    if escolha == 'P':
        if (s % 2) == 0: #Jogador vence
            print('-' * 30)
            print(f'Você jogou {n} e o computador {pc}. Total de {s} DEU PAR')
            print('-' * 30)
            print('Você venceu!')
            print('Vamos jogar novamente...')
            print('-=' * 15)
            vitoria += 1
        else: #Jogador perde
            print('-' * 30)
            print(f'Você jogou {n} e o computador {pc}. Total de {s} DEU ÍMPAR')
            print('-' * 30)
            print('Você perdeu!')
            print('-=' * 15)
            break
    if escolha == 'I':
        if (s % 2) == 0: #Jogador perde
            print('-' * 30)
            print(f'Você jogou {n} e o computador {pc}. Total de {s} DEU PAR')
            print('-' * 30)
            print('Você perdeu!')
            print('-=' * 15)
            break
        else: #Jogador ganha
            print('-' * 30)
            print(f'Você jogou {n} e o computador {pc}. Total de {s} DEU ÍMPAR')
            print('-' * 30)
            print('Você venceu!')
            print('Vamos jogar novamente...')
            print('-=' * 15)
            vitoria += 1
print(f'GAME OVER! Você venceu {vitoria} vezes!')
    