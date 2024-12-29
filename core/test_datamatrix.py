import pytest
from unittest.mock import patch, MagicMock
from PIL import Image

from datamatrix import DatamatrixGenerator


@pytest.fixture
def datamatrix_generator():
    """Fixture para inicializar uma instância do DatamatrixGenerator."""
    return DatamatrixGenerator(output_directory="output")


def test_get_file_path(datamatrix_generator):
    file_name = "test_file"
    path = datamatrix_generator._get_file_path(file_name)
    assert path == "output/test_file.png"

    datamatrix_generator.output_directory = ""
    path = datamatrix_generator._get_file_path(file_name)
    assert path == "test_file.png"


@patch("datamatrix.encode")
def test_create_data_matrix_image(mock_encode, datamatrix_generator):

    mock_encoded_data = MagicMock()
    mock_encoded_data.width = 10
    mock_encoded_data.height = 10
    mock_encoded_data.pixels = b"\x00" * (10 * 10 * 3)
    mock_encode.return_value = mock_encoded_data

    text = "Test DataMatrix"
    image = datamatrix_generator._create_data_matrix_image(text)

    assert isinstance(image, Image.Image)
    assert image.size == (10, 10)

    with pytest.raises(ValueError, match="Input data is empty. Please provide valid input for DataMatrix generation."):
        datamatrix_generator._create_data_matrix_image("")


@patch("datamatrix.Image.Image.save")
@patch("datamatrix.DatamatrixGenerator._create_data_matrix_image")
def test_generate(mock_create_image, mock_save, datamatrix_generator):
    mock_image = MagicMock()
    mock_create_image.return_value = mock_image
    mock_save.return_value = None

    text = "Test DataMatrix"
    file_name = "test_file"
    datamatrix_generator.generate(text, file_name)

    mock_create_image.assert_called_once_with(text)

    expected_path = "output/test_file.png"
    mock_image.save.assert_called_once_with(expected_path)

    mock_create_image.reset_mock()
    mock_create_image.side_effect = Exception("Mocked exception")

    with pytest.raises(Exception, match="Mocked exception"):
        datamatrix_generator.generate(text, file_name)
