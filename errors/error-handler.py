import logging

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ErrorHandler:

    @staticmethod
    def handle_error(e, custom_message=None):
        """
        Trata o erro exibindo uma mensagem personalizada (se fornecida) e registrando o erro.

        :param e: Exceção capturada (Exception)
        :param custom_message: Mensagem personalizada para exibir ao usuário (opcional)
        """
        error_message = f"Erro: {str(e)}"
        if custom_message:
            error_message = f"{custom_message} - Detalhes: {str(e)}"

        print(error_message)
        logging.error(error_message)

def execute_with_error_handling(function, *args, **kwargs):
    """
    Executa uma função com tratamento genérico de exceções.

    :param function: Função a ser executada.
    :param args: Argumentos posicionais da função.
    :param kwargs: Argumentos nomeados (keyword arguments) da função.
    """
    try:
        return function(*args, **kwargs)
    except Exception as err:
        ErrorHandler.handle_error(err, "Um erro ocorreu ao executar a função")
