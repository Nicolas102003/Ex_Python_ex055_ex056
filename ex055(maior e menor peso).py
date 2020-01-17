print('='*5,'P E S O','='*5)
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('digite o peso da {}º pessoas'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg\nO menor peso lido foi de {}Kg'.format(maior ,menor))
