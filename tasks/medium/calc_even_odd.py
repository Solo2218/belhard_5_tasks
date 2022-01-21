"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать программу, которая будет выводить количество четных и нечетных значений
в списке из целых чисел

even - четные
odd - нечетные
"""


def calc_even_odd(array: list) -> tuple:
    even = 0
    odd = 0
    index = 0
    for index in range(len(array)):
        match array[index] % 2:
            case 0:
                even += 1
            case 1:
                odd += 1
    return even, odd


if __name__ == '__main__':
    assert calc_even_odd([2, 1, 5, 4, 7]) == (2, 3)
    print('Решено!')
