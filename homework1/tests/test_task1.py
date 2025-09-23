# task1
from task1 import task_1

def test_say_hello(capsys):
    task_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World"
