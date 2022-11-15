# Подвиг 1. Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список чисел и возвращает их сумму.
#
# Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
# Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:
#
# s = input()
#
# Результат отобразите на экране.

from functools import wraps


#
# s = input()
#
#
# def dec(start):
#     def str_to_int_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             return sum(func(*args, **kwargs)) + start
#         return wrapper
#     return str_to_int_dec
#
#
# @dec(5)
# def str_to_int(s):
#     return list(map(int, s.split()))
#
#
# print(str_to_int(s))

#
# Подвиг 2. Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами).
# Определите декоратор для этой функции, который имеет один параметр tag, определяющий строку с названием тега и начальным значением "h1". Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат.
#
# Пример заключения строки "python" в тег h1: <h1>python</h1>
#
# Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для введенной строки s:
#
# s = input()
#
# Результат отобразите на экране.
#
#
# def low_str_dec(tag='div'):
#     def dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
#         return wrapper
#     return dec
#
#
# @low_str_dec('div')
# def low_str(x):
#     return x.lower()
#
#
# print(low_str('Декораторы - это классно!'))


# Подвиг 3. Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, используя следующий словарь для замены русских букв на соответствующее латинское написание:
#
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку перевести в нижний регистр - малые буквы).
#
# Определите декоратор с параметром chars и начальным значением " !?", который данные символы преобразует в символ "-" и, кроме того, все подряд идущие дефисы (например, "--" или "---") приводит к одному дефису. Полученный результат должен возвращаться в виде строки.
#
# Примените декоратор с аргументом chars="?!:;,. " к функции и вызовите декорированную функцию для введенной строки s:
#
# s = input()
#
# Результат отобразите на экране.


# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# def translate_dec(chars=" !?"):
#     def func_dec(func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             for x in res:
#                 if x in chars:
#                     res = res.replace(x, '-')
#             while '--' in res:
#                 res = res.replace('--', '-')
#             return res
#         return wrapper
#     return func_dec
#
#
# @translate_dec(chars="?!:;,. ")
# def translate(x):
#     return ''.join([t[key] if key in t else key for key in x.lower()])
#
#
# print(translate("Декораторы - это круто!"))


# Подвиг 4. Объявите функцию с именем get_list и следующим описанием в теле функции:
#
# '''Функция для формирования списка целых значений'''
#
# Сама функция должна формировать и возвращать список целых чисел, который поступает на ее вход в виде строки из целых чисел, записанных через пробел.
#
# Определите декоратор, который выполняет суммирование значений из списка этой функции и возвращает результат.
# Внутри декоратора декорируйте переданную функцию get_list с помощью команды @wraps (не забудьте сделать импорт: from functools import wraps). Такое декорирование необходимо, чтобы исходная функция get_list сохраняла свои локальные свойства: __name__ и __doc__.
#
# Примените декоратор к функции get_list, но не вызывайте ее.

from functools import wraps


def sum_dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return sum(func(*args, **kwargs))
    return wrapper


@sum_dec
def get_list(s):
    '''Функция для формирования списка целых значений'''
    return list(map(int, s.split()))


print(get_list("1 2 3 -1 -2 -3"))
