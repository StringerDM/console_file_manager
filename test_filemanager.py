"""
В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше. Это могут быть функции консольного файлового
менеджера, а так же программы мой счет и программы викторина
"""
import os
from bank_account import manage_wallet
from main import get_file_names_list


def test_manage_wallet():
    assert manage_wallet(500, lambda x: x + 500) == 1000
    assert manage_wallet(500, lambda x: x / 500) == 1


def test_get_file_names_list():
    assert get_file_names_list(lambda x: x) == os.listdir(os.getcwd())
