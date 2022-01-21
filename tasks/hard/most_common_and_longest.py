"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""
import collections


def common_and_longest(text: str) -> tuple:
    text = text.split(' ')
    common = collections.Counter(text).most_common(1)
    longest = text[0]
    for index in range(len(text) - 1):
        if len(longest) < len(text[index + 1]):
            longest = text[index + 1]
    return common[0][0], longest


if __name__ == '__main__':
    assert common_and_longest(
        "привет пока ялюблюpython привет"
    ) == ('привет', 'ялюблюpython')
    print('Решено!')
