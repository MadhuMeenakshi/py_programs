import io
import sys

def execute_code(code_str):
    buffer = io.StringIO()
    old_stdout = sys.stdout
    try:
        sys.stdout = buffer
        exec(code_str, {})
    finally:
        sys.stdout = old_stdout
    return buffer.getvalue().strip()

result = execute_code("print(5+2)")  # '7'
