import random
import string
from typing import List, Union

def generate_list_unique_integers(n: int, low: int, up: int) -> List[int]:
    """
    Генерирует список из n уникальных чисел в диапазоне от low до up.

    Параметры:
    n (int): Количество уникальных чисел, которые нужно сгенерировать
    low (int): Нижняя граница диапазона (включительно)
    up (int): Верхняя граница диапазона (включительно)

    Возвращает:
    list[int]: Список, из случайных уникальных чисел

    Исключения:
    ValueError: Если n больше, чем количество возможных уникальных чисел в заданном диапазоне.
    """
    if n > (up - low + 1):
        raise ValueError("Количество уникальных чисел не может превышать диапазон.")

    unique_numbers = random.sample(range(low, up + 1), n)
    return unique_numbers


def generate_list_integers(n: int, low: int, up: int) -> List[int]:
    """
    Генерирует список из n чисел в диапазоне от low до up, допускаются повторы.

    Параметры:
    n (int): Количество чисел, которые нужно сгенерировать
    low (int): Нижняя граница диапазона (включительно)
    up (int): Верхняя граница диапазона (включительно)

    Возвращает:
    list[int]: Список, состоящий из случайных чисел, возможно с повторами.
    """
    numbers = [random.randint(low, up) for _ in range(n)]
    return numbers


def list_to_string(input_list: List[Union[int, str]]) -> str:
    """
    Преобразует список чисел или строк в строку, разделенную пробелами.

    Параметры:
    input_list (list): Список чисел или строк, которые нужно объединить.

    Возвращает:
    str: Строка, содержащая элементы списка, разделенные пробелами.
    """
    return ' '.join(map(str, input_list))


def generate_random_string(length: int, use_digits: bool = True, use_uppercase: bool = True, use_lowercase: bool = True) -> str:
    """
    Генерирует случайную строку заданной длины.

    Параметры:
    length (int): Длина генерируемой строки
    use_digits (bool): Использовать ли цифры в строке
    use_uppercase (bool): Использовать ли заглавные буквы в строке
    use_lowercase (bool): Использовать ли строчные буквы в строке

    Возвращает:
    str: Случайная строка заданной длины.

    Исключения:
    ValueError: Если все параметры использования символов установлены в False.
    """
    if not (use_digits or use_uppercase or use_lowercase):
        raise ValueError("Должен быть выбран хотя бы один тип символов для генерации строки.")

    characters = ''
    if use_digits:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase

    return ''.join(random.choice(characters) for _ in range(length))

def format_arguments(*args: Union[int, str, List[Union[int, str]]]) -> str:
    """
    Форматирует произвольное количество аргументов в строку, разделенную переносами строк.

    Параметры:
    *args: Произвольное количество аргументов, которые могут быть числами, строками или списками.

    Возвращает:
    str: Строка, содержащая все аргументы, разделенные переносами строк.
    """
    formatted_lines = []

    for arg in args:
        if isinstance(arg, list):
            formatted_lines.append(list_to_string(arg))
        else:
            formatted_lines.append(str(arg))

    return '\n'.join(formatted_lines)

def generate_random_integer(low: int, up: int) -> int:
    """
    Генерирует случайное целое число в диапазоне от low до up включительно.

    Параметры:
    low (int): Нижняя граница диапазона (включительно)
    up (int): Верхняя граница диапазона (включительно)

    Возвращает:
    int: Случайное целое число в заданном диапазоне.
    """
    if low > up:
        raise ValueError("Нижняя граница должна быть меньше или равна верхней границе.")

    return random.randint(low, up)

def generate_random_float(low: float, up: float, n: int) -> float:
    """
    Генерирует случайное число с n символами после запятой в диапазоне от low до up.

    Параметры:
    low (float): Нижняя граница диапазона (включительно)
    up (float): Верхняя граница диапазона (включительно)
    n (int): Количество символов после запятой

    Возвращает:
    float: Случайное число с n символами после запятой в заданном диапазоне.
    """
    if low > up:
        raise ValueError("Нижняя граница должна быть меньше или равна верхней границе.")

    random_number = random.uniform(low, up)

    return round(random_number, n)