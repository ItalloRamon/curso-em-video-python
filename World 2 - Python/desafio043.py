peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (pow(altura, 2))
print(f'Seu IMC é {imc:.1f} ')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está  no peso ideal!')
elif 25 <= imc < 30:
    print('Você está no sobrepreso!')
elif 30 <= imc < 40:
    print('Você está com obesidade!')
elif imc >= 40:
    print('Você está com obesidade mórbida!')
