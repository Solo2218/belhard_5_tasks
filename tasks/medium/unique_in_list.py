"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать программу, которая проверит, все ли элементы в списке уникальны

ПРИМЕРЫ
--------------------------------------------------------------------------------
is_unique([2, 1, 5, 4, 7]) -> True
is_unique([2, 1, 5, 4, 2]) -> False
"""


def is_unique(array: list) -> bool:
    result = True
    for index1 in range(len(array)):
        if result:
            for index2 in range(len(array)):
                if index2 != index1:
                    if array[index1] == array[index2]:
                        result = False
                        break
        else:
            break
    return result


if __name__ == '__main__':
    assert is_unique([2, 1, 5, 4, 7])
    assert not is_unique([2, 1, 5, 4, 2])
    print('Решено!')
