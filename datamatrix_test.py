import os
import unittest
from pylibdmtx.pylibdmtx import decode
from PIL import Image
from datamatrix import DatamatrixGenerator

class TestDatamatrixGenerator(unittest.TestCase):
    def setUp(self):
        self.output_directory = "test_output"
        os.makedirs(self.output_directory, exist_ok=True)
        self.generator = DatamatrixGenerator(output_directory=self.output_directory)

    def tearDown(self):
        for file in os.listdir(self.output_directory):
            os.remove(os.path.join(self.output_directory, file))
        os.rmdir(self.output_directory)

    def test_generate_datamatrix(self):
        text = "Hello, DataMatrix!"
        file_name = "test_datamatrix.png"
        file_path = os.path.join(self.output_directory, file_name)

        self.generator.generate(text, file_name)
        self.assertTrue(os.path.exists(file_path))

        img = Image.open(file_path)
        decoded_data = decode(img)
        self.assertEqual(len(decoded_data), 1)
        self.assertEqual(decoded_data[0].data.decode('utf-8'), text)


if __name__ == "__main__":
    unittest.main()
