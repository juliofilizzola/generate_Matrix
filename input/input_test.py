from io import StringIO
import sys
import pyfiglet

from input import print_name_terminal


def test_print_name_terminal_default(monkeypatch):
    captured_output = StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)

    print_name_terminal()

    expected_output = pyfiglet.figlet_format("ASCII")
    assert captured_output.getvalue() == expected_output + '\n'

def test_print_name_terminal_custom_text(monkeypatch):
    captured_output = StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)
    custom_text = "Hello"
    print_name_terminal(custom_text)

    expected_output = pyfiglet.figlet_format(custom_text)
    assert captured_output.getvalue() == expected_output + '\n'