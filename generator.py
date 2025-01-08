from templates import *

def generate_test_input() -> str:
    """Генерирует случайные тестовые данные"""

    n = generate_random_integer(1, 10)
    l = generate_list_integers(n, 1, int(1e9))

    return format_arguments(n, l)
