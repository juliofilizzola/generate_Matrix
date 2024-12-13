import os
import pytest
from pylibdmtx.pylibdmtx import decode
from PIL import Image
from datamatrix import DatamatrixGenerator


@pytest.fixture
def output_directory(tmp_path):
    output_dir = tmp_path / "test_output"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


@pytest.fixture
def generator(output_directory):
    return DatamatrixGenerator(output_directory=output_directory)


def test_generate_datamatrix(generator, output_directory):
    text = "Hello, DataMatrix!"
    file_name = "test_datamatrix.png"
    file_path = os.path.join(output_directory, file_name)

    generator.generate(text, file_name)

    assert os.path.exists(file_path)

    img = Image.open(file_path)
    decoded_data = decode(img)

    assert len(decoded_data) == 1
    assert decoded_data[0].data.decode('utf-8') == text
