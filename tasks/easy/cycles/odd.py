"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая принимает список, который может содержать различные
данных.
В функции создается новый список.
Если элемент переданного списка - четное число, то добавить его в созданный список.
Необходимо вернуть созданный список

Пропуск элементов сделать с помощью continue

ПРИМЕРЫ
--------------------------------------------------------------------------------
odd_in_list([1, False, 2, -1, 'Hi', 4, 6, [], (), -8]) -> [2, 4, 6, -8]
odd_in_list([2, -1, 4, True, None, 6]) -> [2, 4, 6]
"""
some_list1 = []


def odd_in_list(some_list: list) -> list:
    odd_list = []
    index = 0
    for index in range(len(some_list)):
        if isinstance(some_list[index], bool):
            continue
        elif isinstance(some_list[index], int):
            if some_list[index] % 2 == 0:
                odd_list.append(some_list[index])
    return odd_list


if __name__ == '__main__':
    assert odd_in_list([1, False, 2, -1, 'Hi', 4, 6, [], (), -8]) == [2, 4, 6, -8]
    print('Решено!')
