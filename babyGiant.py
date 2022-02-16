from math import sqrt, ceil
from traceback import format_exc


def getM(p):
    less = int(sqrt(p))
    more = less + 1
    return (less if p - (less ** 2) < (more ** 2) - p else more) + 1


def bsStep(a, b, p):
    m = getM(p)
    k = int(ceil(p / m))
    j = 0
    i = 1
    smallList = []
    bigList = []
    while j < m:
        x = ((a ** j) * b) % p  # считаем (a^j)*b
        smallList.append((j, x))  # добавляем результат в лист кортежей
        j += 1
    print('(a^j)*b>>>', smallList)
    while i <= m * k:
        x = (a ** (i * m)) % p  # считаем a^(i*m)
        bigList.append((i, x))  # добавляем результат в лист кортежей
        i += 1
    print('a^(i*m)>>>', bigList)
    for el1 in range(len(bigList)):
        for el2 in range(len(smallList)):
            if smallList[el2][1] == bigList[el1][1]:  # находим первое совпадение
                j = smallList[el2][0]
                i = bigList[el1][0]
                return j, i, i * m - j
    else:
        raise ValueError('No match found')


if __name__ == '__main__':
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    p = int(input('Введите p: '))
    print(f'Ваше уравнение -> ({a}^x) ≡ {b}(mod {p})'.format(a, b, p))
    try:
        j, i, x = bsStep(a, b, p)
        print(f'j = {j}, i = {i}, x = {x}'.format(j, i, x))
    except ValueError:
        print(format_exc())
    finally:
        input('Нажмите любую кнопку...')
