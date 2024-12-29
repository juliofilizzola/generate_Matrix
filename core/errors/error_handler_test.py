import pytest
from errors.error_handler import ErrorHandlerCustom
import logging
def test_handle_error_with_custom_message(caplog):
    with caplog.at_level(logging.ERROR):
        ErrorHandlerCustom.handle_error(Exception("Test error"), "Custom message")
    assert "Custom message - Detalhes: Test error" in caplog.text

def test_handle_error_without_custom_message(caplog):
    with caplog.at_level(logging.ERROR):
        ErrorHandlerCustom.handle_error(Exception("Test error"))
    assert "Erro: Test error" in caplog.text