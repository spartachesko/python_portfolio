# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.n, self.a = n, 1

    def __iter__(self):
        self.a = 1
        self.prime_numbers = []
        return self

    def __next__(self):
        self.a += 1
        if self.a < self.n:
            for self.a in range(self.a, self.n + 1):
                for prime in self.prime_numbers:
                    if self.a % prime == 0:
                        break
                else:
                    self.prime_numbers.append(self.a)
                    return self.a

        raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)


# после подтверждения части 1 преподователем, можно делать

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number
    return prime_numbers


for number in prime_numbers_generator(n=10000):
    print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
#  Импорты должны находиться в самом начале файла.


def checking_lucky_numbers(value):
    value = str(value)
    middle_value = int(len(value) / 2)
    left_sum = 0
    right_sum = 0
    count_left = 0
    if len(value) % 2 != 0:
        count_right = middle_value + 1

    else:
        count_right = middle_value

    for number_left in range(0, int(middle_value)):
        left_sum += int(value[count_left])
        count_left += 1
    for number_right in range(int(count_right), int(len(value))):
        right_sum += int(value[count_right])
        count_right += 1
    result = (left_sum == right_sum)
    return result


def checking_palindrome_numbers(value):
    value = str(value)
    value_reverse = value[::-1]
    result = value == value_reverse
    return result


def checking_automorphic_number(value):
    square_value = value ** 2
    result = str(square_value).endswith(str(value))
    # Автоморфное число — число, десятичная запись квадрата
    # которого оканчивается цифрами самого этого числа.
    return result


value_for_checking = 626
checking_lucky_numbers(value=value_for_checking)
checking_palindrome_numbers(value=value_for_checking)
checking_automorphic_number(value=value_for_checking)

list_of_checking = [checking_lucky_numbers,
                    checking_palindrome_numbers,
                    checking_automorphic_number]

n = 100


def check_generator(to_num, fn_arr):
    prime_numbers = []
    for number in range(2, to_num + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break

        else:
            prime_numbers.append(number)
            for fn in fn_arr:
                if not fn(number):
                    break
            else:
                yield number

    return prime_numbers


for num in check_generator(to_num=10000, fn_arr=list_of_checking):
    print(f'Число является счастливым, полиндромным и автоморфным- {num}')

list_of_checking = [checking_lucky_numbers,
                    checking_palindrome_numbers,
                    checking_automorphic_number]

gen_values = filter(checking_lucky_numbers, filter(checking_palindrome_numbers, prime_numbers_generator(1000)))
for number in gen_values:
    print(f'Число является счастливым, полиндромным и автоморфным- {number}')
