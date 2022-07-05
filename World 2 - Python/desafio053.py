s = str(input('Digite uma frase: ')).upper().strip().replace(' ', '')
reverso = list(reversed(s))
i = 0
print(f'O contrário de {s} é {s[::-1]}')
for c in range(0, len(s)):
    if s[c] == reverso[c]:
        i += 1
if i == len(s):
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')