import pyfiglet

ascii = "ASCII"

def print_name_terminal(text: str = ascii) -> None:
    terminal_print = pyfiglet.figlet_format(text)
    print(terminal_print)