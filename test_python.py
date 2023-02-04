"""
2. В модуле написать тесты для встроенных функций filter, map, sorted, а также для функций из библиотеки math: pi, sqrt,
 pow, hypot. Чем больше тестов на каждую функцию - тем лучше
"""
import math


def test_filter():
    assert list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])) == [2, 4, 6]
    assert list(filter(lambda x: len(x) > 3, ['g', 'df', 'привет', 'как', 'дела'])) == ['привет', 'дела']


def test_map():
    assert list(map(lambda x: x * 2, [1, 2, 3, 4, 5, 6])) == [2, 4, 6, 8, 10, 12]
    assert list(map(lambda s: s * 2, ['a', 'b', 'c'])) == ['aa', 'bb', 'cc']


def test_sorted():
    test_list = [1, 2, 67, 23, 12]
    assert sorted(test_list) == [1, 2, 12, 23, 67]
    assert sorted(test_list, reverse=True) == [67, 23, 12, 2, 1]

    test_list = ['один', 'два', 'три']
    assert sorted(test_list, key=len) == ['два', 'три', 'один']


def test_math_pi():
    assert math.pi == 3.141592653589793


def test_math_sqrt():
    assert math.sqrt(4) == 2


def test_math_pow():
    assert math.pow(4, 2) == 16


def test_math_hypot():
    assert math.hypot(3, 4) == 5


