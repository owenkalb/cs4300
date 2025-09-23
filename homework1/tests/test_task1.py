# Task1 test
from task1 import task_1

# Check if hello world printed
def test_say_hello(capsys):
    task_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World"
