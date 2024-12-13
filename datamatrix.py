from pylibdmtx.pylibdmtx import encode
from PIL import Image


class DatamatrixGenerator:
    def __init__(self, output_directory=""):
        self.output_directory = output_directory

    def generate(self, text, name_file) -> None:
        try:
            datamatrix = encode(text.encode('utf-8'))

            img = Image.frombytes('RGB', (datamatrix.width, datamatrix.height), datamatrix.pixels)

            path = f"{self.output_directory}/{name_file}" if self.output_directory else name_file

            img.save(path)
            print(f"DataMatrix generate and save {path}.")
        except Exception as e:
            print(f"err in generate DataMatrix: {e}")