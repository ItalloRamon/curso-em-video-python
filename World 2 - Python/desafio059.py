n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
opcao = int(input('Qual a sua opção? '))
while opcao != 5:
    if opcao == 1:
        print(f'A soma do números é {n1 + n2}')
    elif opcao == 2:
        print(f'O produto dos números é {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n1 < n2:
            print(f'O maior número é {n2}')
        else:
            print('Os números são iguais!')
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Opção inválida!')
    
    print('-=' * 15)
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    
    opcao = int(input('Qual a sua opção? '))

print('Fim do programa!')    
