import pytest
import pytest_mock
from unittest.mock import ANY
from datamatrix import DatamatrixGenerator
from errors.error_handler import ErrorHandlerCustom

def test_generate_handles_error(mocker):
    generator = DatamatrixGenerator()
    mock_handle_error = mocker.patch.object(ErrorHandlerCustom, 'handle_error')

    generator.generate("", "test_file")

    # Verifica se a função handle_error foi chamada uma vez
    mock_handle_error.assert_called_once()
    # Verifica se a função handle_error foi chamada com os argumentos corretos
    mock_handle_error.assert_called_with(ANY, "Error generating DataMatrix")