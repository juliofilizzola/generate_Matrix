from getTerminalInput import get_terminal_input

def test_get_terminal_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'test input')
    assert get_terminal_input('Enter something: ') == 'test input'