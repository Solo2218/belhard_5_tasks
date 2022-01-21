"""
Проверить, является ли число степенью двойки.
Вернуть True или False

is_pow_2(1) -> True
is_pow_2(2) -> True
is_pow_2(16) -> True
is_pow_2(256) -> True
is_pow_2(1024) -> True
is_pow_2(13) -> False
is_pow_2(17) -> False
"""


def is_pow_2(number) -> bool:
    i = 0
    result = None
    if number == 1:
        result = True
    elif number % 2 == 0:
        while 2 ** i <= number:
            if 2 ** i < number:
                i += 1
                result = False
            elif 2 ** i == number:
                result = True
                break
    else:
        result = False
    return result


if __name__ == '__main__':
    assert is_pow_2(4)
    assert is_pow_2(16)
    assert is_pow_2(256)
    assert not is_pow_2(123)
    print("Решено")
