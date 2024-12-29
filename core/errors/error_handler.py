import logging

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ErrorHandlerCustom:

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
