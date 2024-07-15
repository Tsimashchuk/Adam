import pytest

from src.decorators import log, my_function


def test_log_good():                      # Положительный исход
    @log(filename='log_file.txt')
    def func(x, y):
        return x + y

    result = func(3, 0)
    assert result == 3


def test_log_exception():                 # Выбрасывает исключение
    with pytest.raises(Exception):
        my_function()
