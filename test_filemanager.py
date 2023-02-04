"""
В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше. Это могут быть функции консольного файлового
менеджера, а так же программы мой счет и программы викторина
"""

from bank_account import manage_wallet


def test_manage_wallet():
    assert manage_wallet(500, lambda x: x + 500) == 1000
    assert manage_wallet(500, lambda x: x / 500) == 1