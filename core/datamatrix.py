from pylibdmtx.pylibdmtx import encode
from errors.error_handler import execute_with_error_handling
from PIL import Image


class DatamatrixGenerator:

    def __init__(self, output_directory=""):
        self.output_directory = output_directory

    def generate(self, text, file_name) -> None:
        try:
            image = self._create_data_matrix_image(text)
            print(f"Generating DataMatrix for: {text}")
            file_path = self._get_file_path(file_name)
            image.save(file_path)
            print(f"DataMatrix successfully generated and saved at: {file_path}")
        except Exception as e:
            print(f"Error generating DataMatrix: {e}")
            execute_with_error_handling(e, "Error generating DataMatrix")

    @staticmethod
    def _create_data_matrix_image(text: str) -> Image:
        if not text:
            raise ValueError("Input data is empty. Please provide valid input for DataMatrix generation.")
        encoded_data_matrix = encode(text.encode('utf-8', 'ignore'))

        return Image.frombytes('RGB', (encoded_data_matrix.width, encoded_data_matrix.height), encoded_data_matrix.pixels)

    def _get_file_path(self, file_name: str) -> str:
        return f"{self.output_directory}/{file_name}.png" if self.output_directory else f"{file_name}.png"
