# Подвиг 2. Вводится целое положительное число N. Необходимо написать рекурсивную функцию с именем get_rec_N, которая отображает на экране последовательность целых чисел от 1 до N (включительно). Каждое число выводится с новой строки.

# В качестве параметра функция get_rec_N должна принимать одно числовое значение. То есть, иметь только один параметр. Начальный вызов функции будет выглядеть так:

# get_rec_N(N)
# Вызывать функцию не нужно, только объявить.

# считывание числа N
# N = int(input())

# здесь продолжайте программу
# def get_rec_N(N):
#    if N == 0:
#        return
#    else:
#        get_rec_N(N-1)
#        print(N)


# Подвиг 3. Вводится список целых чисел в одну строчку через пробел. Необходимо вычислить сумму этих введенных значений, используя рекурсивную функцию (для перебора элементов списка) с именем get_rec_sum. Функция должна возвращать значение суммы. (Выводить на экран она ничего не должна).

# Вызовите эту функцию и выведите вычисленное значение суммы на экран.

# enter = list(map(int, input().split()))
# summ = 0


# def get_rec_sum(enter):
#    if len(enter) == 1:
#        return enter[0]
#    else:
#        return enter[0] + get_rec_sum(enter[1:])


# print(get_rec_sum(enter))


# Подвиг 4. Вводится натуральное число N. Необходимо с помощью рекурсивной функции fib_rec(N, f=[]) (здесь N - общее количество чисел Фибоначчи; f - начальный список этих чисел) сформировать последовательность чисел Фибоначчи по правилу: первые два числа равны 1 и 1, а каждое следующе значение равно сумме двух предыдущих. Пример такой последовательности для первых 7 чисел: 1, 1, 2, 3, 5, 8, 13, ...

# Функция должна возвращать список сформированной последовательности длиной N.

# Вызывать функцию не нужно, только объявить.


# ввод числа N
# N = int(input())

# здесь задается функция fib_rec (переменную N не менять!)

# def fib_rec(N, f=[1,1]):
#    if N <= 2:
#        return f
#    else:
#        fib_rec((N-1),f)
#        f.append(f[-2] + f[-1])
#    return f


# fib_rec(N, f=[1,1])


# Подвиг 5. Вводится целое неотрицательное число n. Необходимо с помощью рекурсивной функции fact_rec вычислить факториал числа n. Напомню, что факториал числа, равен: n! = 1 * 2 * 3 *...* n. Функция должна возвращать вычисленное значение.
# Вызывать функцию не нужно, только объявить со следующей сигнатурой:

# def fact_rec(n): ...


# ввод числа n
# n = int(input())

# здесь задается функция fact_rec  (переменную n не менять!)

# def fact_rec(n):
#    assert n >= 0, "Factorial of negative number error "
#    if n == 0:
#        return  1
#    return n * fact_rec(n-1)


# print(fact_rec(n))


# Подвиг 6. Имеется следующий многомерный список:
#
# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# С помощью рекурсивной функции get_line_list создать на его основе одномерный список из значений элементов списка d. Функция должна возвращать новый созданный одномерный список.  (Только возвращать, выводить на экран ничего не нужно.)
#
# Вызывать функцию не нужно, только объявить со следующей сигнатурой:
#
# def get_line_list(d,a=[]): ...
# где d - исходный список; a - новый формируемый.

# def get_line_list(d, a=[]):
#     for x in d:
#         if type(x) == list:
#             d = x
#             get_line_list(d, a)
#         else:
#             a.append(x)
#     return a
#
# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# print(get_line_list(d, a=[]))


# Подвиг 7. Лягушка прыгает вперед и может скакнуть либо на одно деление, либо сразу на два. Наша задача определить количество вариантов маршрутов, которыми лягушка может достичь риски под номером N (натуральное число N вводится с клавиатуры).
#
#
#
# Решать задачу следует с применением рекурсивной функции. Назовем ее get_path. Алгоритм решения будет следующий. Рассмотрим, например, риску под номером 4. Очевидно, в нее лягушка может скакнуть либо с риски номер 2, либо с риски номер 3. Значит, общее число вариантов перемещений лягушки можно определить как:
#
# get_path(4) = get_path(3) + get_path(2)
#
# Аналогично будет справедливо и для любой риски N:
#
# get_path(N) = get_path(N-1) + get_path(N-2)
#
# А начальные условия задачи, следующие:
#
# get_path(1) = 1
# get_path(2) = 2
#
# Реализуйте такую рекурсивную функцию, которая должна возвращать количество вариантов перемещений лягушки для риски под номером N.
#
# Вызовите эту функцию для введенного числа N и отобразите результат на экране.


# def get_path(N):
#     res = 1
#     if N == 2:
#         return 2
#     elif N == 1:
#         return 1
#     else:
#         res = get_path(N-1) + get_path(N-2)
#     return res
#
#
# print(get_path(4))


# Великий подвиг 8. Вводится список из целых чисел в одну строчку через пробел. Необходимо выполнить его сортировку по возрастанию с помощью алгоритма сортировки слиянием. Функция должна возвращать новый отсортированный список.
# Вызовите результирующую функцию сортировки для введенного списка и отобразите результат на экран в виде последовательности чисел, записанных через пробел.
#
# Подсказка. Для разбиения списка и его последующей сборки используйте рекурсивные функции.
#
# P.S. Теория сортировки в видео предыдущего шага.

def sort_m(A):
    i = k = n = 0
    res = [0] * len(A)
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range[:middle]]
    R = [A[i] for i in range[middle:len(A)]]
    sort_m(L)
    sort_m(R)
    while i < len(L) and k < len(R):
        if L[i] <= R[k]:
            res[n] = L[i]
            i += 1
            n += 1
        else:
            res[n] = R[k]
            k += 1
            n += 1
    while i < len(L):
        res[n] = L[i]
        i += 1
        n += 1
    while k < len(R):
        res[n] = R[k]
        k += 1
        n += 1
    return res

print(sort_m([-2,-3,0,1,6,10]))
