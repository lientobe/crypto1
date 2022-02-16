from traceback import format_exc


def isPrime(num):  # число простое или нет
    for el in range(2, num):
        if (num / el) % 1 == 0:
            return False
    return True


def inBin(degree):  # перевод числа в двоичный вид
    b = ''
    while degree > 0:
        b = str(degree % 2) + b
        degree = degree // 2
    return b[1:]


def findPrimeNums(p, g):  # проверка что g может быть корнем(по 3 пунктам: p<3,
    numList = []  # (p/g)%1==0, g^((p-1)/p)(mod p) != 1)
    if (p / g) % 1 == 0 or p < 3:
        return True
    chP = p - 1
    primeNumber = 2
    while not isPrime(chP):
        if (chP / primeNumber) % 1 == 0:
            numList.append(primeNumber)
            chP //= primeNumber
        else:
            primeNumber += 1
    else:
        numList.append(chP)  # numList содержит множители p (простые)
    for i in range(len(numList)):  # g^((p-1)/p)(mod p) != 1
        if binAlg(g, (p - 1) // numList[i], p) == 1:
            return True
    return False


def DiffiHell(xA, xB, p, g):
    if findPrimeNums(p, g):
        raise ValueError("g не первичный корень")
    yA = binAlg(g, xA, p)  # находим yA
    yB = binAlg(g, xB, p)  # находим yB
    s1 = binAlg(yB, xA, p)  #
    s2 = binAlg(yA, xB, p)  # находим s1 и s2 (должны совпасть)

    if s1 != s2:
        raise ValueError('Ключи не совпадают')  # если не совпали, кидаем исключение
    return s1


def binAlg(a, b, p):  # бинарный алгоритм
    varInBin = inBin(b)
    chA = a
    for el in varInBin:
        chA = ((chA ** 2) * (a ** int(el))) % p
    return chA


if __name__ == '__main__':
    xA = int(input('Введите xA: '))
    xB = int(input('Введите xB: '))
    p = int(input('Введите p: '))
    g = int(input('Введите g: '))
    try:
        print('Общий ключ ->', DiffiHell(xA, xB, p, g))
    except ValueError:
        print(format_exc())
    finally:
        input("Нажмите любую кнопку...")
