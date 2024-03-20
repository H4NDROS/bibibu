def digit(n):
    k = 0
    while n>0:
        k += 1
        n //= 10
    print('Кол-во цифр:',k)
    return n
n = int(input('Введите число: '))
digit(n)