# task1
from task1 import say_hello

def test_say_hello(capsys):
    say_hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World"
