import subprocess
import os

def compile_cpp_program(program_path: str) -> None:
    """Компилирует C++ программу по указанному пути."""
    compile_command = f"g++ {program_path} -o {os.path.splitext(program_path)[0]}"
    process = subprocess.run(compile_command, shell=True, text=True, capture_output=True)

    if process.returncode != 0:
        raise RuntimeError(f"Ошибка компиляции {program_path}:\n{process.stderr}")


def run_cpp_program(program_path: str, input_data: str) -> tuple[str, str]:
    """Запускает скомпилированную C++ программу с входными данными."""
    process = subprocess.Popen(
        program_path,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    output, error = process.communicate(input=input_data)
    return output.strip(), error.strip()
