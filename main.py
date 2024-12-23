from core.datamatrix import DatamatrixGenerator
from input.getTerminalInput import get_terminal_input

def main():
    name_file = get_terminal_input("Digite o nome do arquivo: ")
    message = get_terminal_input("Digite a mensagem para o DataMatrix: ")

    datamatrix = DatamatrixGenerator()
    datamatrix.generate(message, name_file)

if __name__ == "__main__":
    main()