#Подвиг 2. Объявите анонимную (лямбда) функцию с одним параметром для возведения числа в квадрат. Присвойте эту функцию переменной get_sq.

# Вызывать функцию не нужно, только задать.


# get_sq = lambda a: a**2
#
# print(get_sq(7))
#
# Подвиг 3. Объявите анонимную (лямбда) функцию с двумя параметрами для деления одного целого числа на другое. Если происходит деление на ноль, то функция должна возвращать значение None, иначе - результат деления.
#
# Присвойте эту функцию переменной get_div. Вызывать функцию не нужно, только задать.

# s = lambda a, b: None if a == 0 or b == 0 else a / b
# print(s(10, 0))

# Подвиг 5. Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "ra". То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.
#
# Вызовите эту функцию для введенной строки s:
#
# s = input()
#
# Отобразите результат работы функции на экране.

s= input()
z = lambda s: "ra" in s
print(z(s))
