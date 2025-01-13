import pytest
from unittest.mock import patch, MagicMock
from PIL import Image
import os
from datamatrix import DatamatrixGenerator
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


@pytest.fixture
def datamatrix_generator():
    return DatamatrixGenerator()


def test_get_file_path(datamatrix_generator):
    file_name = "test_file"
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


def test_generate_success(datamatrix_generator):
    text = "Test DataMatrix"
    file_name = "test"
    datamatrix_generator.generate(text, file_name)

    path = datamatrix_generator._get_file_path(file_name)
    assert path == "test.png"

    image = Image.open("test.png")
    assert image.format == "PNG"
    image.close()
    os.remove("test.png")
