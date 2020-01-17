nommasc = 0
idmasc = ''
femi = 0
idades = 0
for p in range(1, 5):
    print('===== {}º pessoa ====='.format(p))
    nome = str(input('Nome')).strip()
    id = int(input('Idade'))
    sexo = str(input('Sexo (M/F)')).strip()
    idades += id
    if sexo in 'Mm':
        idmasc = id
        nommasc = nome
    if sexo in 'Mm' and id > idmasc:
        idmasc = id
        nommasc = nome
    if sexo in 'Ff' and id < 20:
        femi += 1
print('A media de idades é {}'.format(idades / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(idmasc, nommasc))
print('Ao todo tem {} mulheres com menos de 20 anos'.format(femi))