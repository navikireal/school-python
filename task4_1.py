mera = 1.0
k = 1.0
smdm = 2.54
milkm = 1.61
kgfun = 0.45
grunc = 28.35
def pr(mera, k):
    pr = mera * k
    return pr
def dr(mera, k):
    dr = mera / k
    return dr
i = ''
while i != '0':
    print('1. Дюймы в сантиметры\n'
          '2. Сантиметры в дюймы\n'
          '3. Мили в километры\n'
          '4. Километры в мили\n'
          '5. Фунты в килограммы\n'
          '6. Килограммы в фунты\n'
          '7. Унции в граммы\n'
          '8. Граммы в унции\n')
    i = input(f'Выберите функцию :\n')
    if i.isdigit() == False:
        print('Ошибка')
    elif i == '1' :
        x = float(input(f'Введите дюймы: '))
        print('сантиметров = ', pr(x, smdm))
    elif i == '2' :
        x = float(input(f'Введите сантиметры: '))
        print('дюймов = ', dr(x, smdm))
    elif i == '3' :
        x = float(input(f'Введите мили: '))
        print('километров = ', pr(x, milkm))
    elif i == '4' :
        x = float(input(f'Введите километры: '))
        print('милей = ', dr(x, milkm))
    elif i == '5' :
        x = float(input(f'Введите фунты: '))
        print('килограмм = ', pr(x, kgfun))
    elif i == '6' :
        x = float(input(f'Введите килограммы: '))
        print('фунтов = ', dr(x, kgfun))
    elif i == '7':
        x = float(input(f'Введите унции: '))
        print('грамм = ', pr(x, grunc))
    elif i == '8':
        x = float(input(f'Введите граммы: '))
        print('унций = ', pr(x, grunc))
    else:
        print('ошибка')