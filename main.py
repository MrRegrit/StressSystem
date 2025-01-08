import os
import shutil

from cpp_runner import compile_cpp_program, run_cpp_program
from generator import generate_test_input

def main():
    solution_path = 'CppPrograms/solution.cpp'
    answer_path = 'CppPrograms/answer.cpp'

    compile_cpp_program(solution_path)
    compile_cpp_program(answer_path)

    num_tests = 100
    user_input = input(f"Введите количество тестов (по умолчанию {num_tests}): ")
    if user_input.strip():
        num_tests = int(user_input)

    tests_dir = 'Tests'
    if os.path.exists(tests_dir):
        shutil.rmtree(tests_dir)

    os.makedirs(tests_dir)


    for test in range(1, num_tests + 1):
        test_input = generate_test_input()
        output_solution, error_solution = run_cpp_program('CppPrograms/solution', test_input)
        output_answer, error_answer = run_cpp_program('CppPrograms/answer', test_input)

        test_folder = os.path.join(tests_dir, f'Test #{test}')
        os.makedirs(test_folder, exist_ok=True)

        with open(os.path.join(test_folder, 'input.txt'), 'w') as f:
            f.write(test_input)

        with open(os.path.join(test_folder, 'solution.txt'), 'w') as f:
            f.write(output_solution)

        with open(os.path.join(test_folder, 'answer.txt'), 'w') as f:
            f.write(output_answer)

        if error_solution or error_answer:
            print(f"Ошибка в одной из программ на тесте {test}: {error_solution if error_solution else error_answer}")
            return

        if output_solution != output_answer:
            print(f"Тест {test} не прошел:\n{test_input}\n------\n"
                  f"Решение: \n{output_solution}\n------\n"
                  f"Тестируемая программа: \n{output_answer}")
            return

    print("Все тесты прошли успешно.")

if __name__ == "__main__":
    main()
