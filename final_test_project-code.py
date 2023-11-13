print("Привет, данная программа выполняет ряд следующих функций: ")
print("1 - Приветствие")
print("2 - НОК и НОД двух чисел")
print("3 - Статистические данные")
print("4 - Сумма кодбов и факториалов")
print("5 - Пропущенное число")
print("6 - N-ое число Фибоначчи")
print("7 - Наиболшее количество подряд идущих чисел равных друг другу и само число")
print("8 - Степень двойки")
print("9 - Улитка")
print("10 - Часы")


# task 1
def greeting():
    name = input("Введите свое имя: ")
    age = int(input("Введите свой возраст: "))
    if age < 7:
        print("Hello, " + name + "! You are too young to study.")
    elif age <= 17:
        grade = age - 6
        experience = max(0, grade - 8)
        print("Hello, " + name + "! You are at " + str(grade) + " grade and have " + str(
            experience) + " years of programming experience. Sounds cool!")
    elif age <= 21:
        course = age - 17
        experience = course + 3
        print("Hello, " + name + "! You are at " + str(course) + " course and have " + str(
            experience) + " years of programming experience. Sounds cool!")
    else:
        print("Hello, " + name + "! You are entrepreneur and have 7 years of programming experience. Sounds cool!")


# task 2
def gcd_and_lcm():
    a, b = map(int, input("Введите два целых числа через пробел: ").split())
    # Находим НОД по алгоритму Евклида
    x = a
    y = b
    while y != 0:
        x, y = y, x % y
    gcd = x
    # Находим НОК по формуле НОК(a, b) = a * b / НОД(a, b)
    lcm = a * b // gcd
    print("НОД =", gcd)
    print("НОК =", lcm)


# task 3
def statistics():
    n, k = map(int, input("Введите n и k через пробел: ").split())
    # Считываем n чисел в список
    numbers = []
    for i in range(n):
        numbers.append(int(input("Введите число: ")))
    # Проверяем, что k не больше n
    if k > n:
        print("k не может быть больше n")
        return
    # Вычисляем среднее арифметическое по формуле S = (a1 + ... + ak) / k
    arithmetic_mean = sum(numbers[:k]) / k
    # Вычисляем среднее гармоническое по формуле H = k / (1/a1 + ... + 1/ak)
    harmonic_mean = k / sum(1 / x for x in numbers[:k])
    # Находим максимальный и второй максимальный элементы
    max_element = max(numbers[:k])
    second_max_element = max(x for x in numbers[:k] if x != max_element)
    # Находим минимальный и второй минимальный элементы
    min_element = min(numbers[:k])
    second_min_element = min(x for x in numbers[:k] if x != min_element)
    # Выводим результаты
    print("Среднее арифметическое =", arithmetic_mean)
    print("Среднее гармоническое =", harmonic_mean)
    print("Максимальный элемент =", max_element)
    print("Второй максимальный элемент =", second_max_element)
    print("Минимальный элемент =", min_element)
    print("Второй минимальный элемент =", second_min_element)


# task 4
def sums():
    n = int(input("Введите натуральное число n: "))
    # Проверяем, что n положительно
    if n <= 0:
        print("n должно быть больше 0")
        return
    # Вычисляем сумму кубов по формуле S = (n * (n + 1) / 2)  2
    sum_of_cubes = (n * (n + 1) // 2)
    # Вычисляем сумму факториалов по рекуррентной формуле F(n) = n! + F(n - 1), F(1) = 1
    sum_of_factorials = 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
        sum_of_factorials += factorial
    # Выводим результаты
    print("Сумма кубов =", sum_of_cubes)
    print("Сумма факториалов =", sum_of_factorials)


# task 5
def missing_number():
    n = int(input("Введите натуральное число n: "))
    # Проверяем, что n положительно
    if n <= 0:
        print("n должно быть больше 0")
        return
    # Считываем n - 1 чисел в множество
    numbers = set()
    for i in range(n - 1):
        numbers.add(int(input("Введите число от 1 до n: ")))
    # Находим пропущенное число как разность суммы арифметической прогрессии и суммы множества
    missing = n * (n + 1) // 2 - sum(numbers)
    print("Пропущенное число =", missing)


# task 6
def fibonacci():
    n = int(input("Введите целое число n: "))
    # Проверяем, что n неотрицательно
    if n < 0:
        print("n должно быть больше или равно 0")
        return
    # Вычисляем n-ое число Фибоначчи по рекуррентной формуле F(n) = F(n - 1) + F(n - 2), F(0) = 0, F(1) = 1
    # Используем динамическое программирование для оптимизации
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    print("n-ое число Фибоначчи =", fib[n])


# task 7
def longest_sequence():
    # Считываем последовательность чисел в список
    numbers = []
    while True:
        word = input("Введите число или end: ")
        if word == "end":
            break
        else:
            numbers.append(int(word))
    # Проверяем, что список не пустой
    if not numbers:
        print("Последовательность пустая")
        return
    # Ищем наибольшее количество подряд идущих чисел равных друг другу и само число
    # Используем два указателя для подсчета длины текущей и максимальной последовательности
    max_length = 1
    max_number = numbers[0]
    current_length = 1
    current_number = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] == current_number:
            current_length += 1
        else:
            current_length = 1
            current_number = numbers[i]
        if current_length > max_length:
            max_length = current_length
            max_number = current_number
    print("Наибольшее количество подряд идущих чисел равных друг другу =", max_length)
    print("Само число =", max_number)

    # task 8


def highest_power_of_two():
    n = int(input("Введите натуральное число n: "))
    # Проверяем, что n положительно
    if n <= 0:
        print("n должно быть больше 0")
        return
    # Ищем наибольшую целую степень двойки, не превосходящую n
    # Используем бинарные операции для оптимизации
    # Сдвигаем n вправо, пока не получим 0, и запоминаем количество сдвигов
    shifts = 0
    while n > 0:
        n >>= 1
        shifts += 1
    # Сдвигаем 1 влево на количество сдвигов минус 1, чтобы получить искомую степень двойки
    power_of_two = 1 << (shifts - 1)
    print("Наибольшая целая степень двойки, не превосходящая n =", power_of_two)

    # task 9


# task 9
def snail():
    # Считываем три целых числа больше 0 через ";"
    h, a, b = map(int, input("Введите h, a, b через ';': ").split(";"))
    # Проверяем, что a больше b
    if a <= b:
        print("a должно быть больше b")
        return
    # Вычисляем, на какой день улитка выползет из ямы
    # Используем формулу d = ceil((h - a) / (a - b)) + 1
    from math import ceil
    d = ceil((h - a) / (a - b)) + 1
    print("Улитка выползет из ямы на", d, "день")


# task 10
def clock():
    # Считываем дробное число a
    a = float(input("Введите угол в градусах: "))
    # Проверяем, что a неотрицательно и не больше 360
    if a < 0 or a > 360:
        print("a должно быть в диапазоне от 0 до 360")
        return
    # Вычисляем, сколько полных часов, минут и секунд прошло с начала суток
    # Используем формулы h = floor(a / 30), m = floor((a % 30) * 2), s = floor(((a % 30) * 2 - m) * 30)
    from math import floor
    h = floor(a / 30)
    m = floor((a % 30) * 2)
    s = floor(((a % 30) * 2 - m) * 30)
    print(h, m, s, sep=",")


while True:
    choice = int(input("Введите число от 1 до 10 - номер функции: "))
    if 1 > choice < 10:
        print("Такой функции нет, введите корректный номер функции")
    elif choice == 1:
        greeting()
    elif choice == 2:
        gcd_and_lcm()
    elif choice == 3:
        statistics()
    elif choice == 4:
        sums()
    elif choice == 5:
        missing_number()
    elif choice == 6:
        fibonacci()
    elif choice == 7:
        longest_sequence()
    elif choice == 8:
        highest_power_of_two()
    elif choice == 9:
        snail()
    elif choice == 10:
        clock()
