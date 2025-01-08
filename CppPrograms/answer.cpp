#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    // Генерация случайного числа для определения порядка сортировки
    std::random_device rd;  // Получаем случайное число
    std::mt19937 gen(rd()); // Инициализируем генератор
    std::uniform_int_distribution<> dis(1, 100); // Генератор случайных чисел от 1 до 100

    int random_value = dis(gen);

    if (random_value == 1) {
        // Сортировка в порядке убывания
        std::sort(numbers.begin(), numbers.end(), std::greater<int>());
    } else {
        // Сортировка в порядке возрастания
        std::sort(numbers.begin(), numbers.end());
    }

    // Вывод отсортированных чисел
    for (const int& num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
