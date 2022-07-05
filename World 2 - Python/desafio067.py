while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 40)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
    print('-' * 40)
print('Programa Tabuada encerrado... Volte sempre!')
