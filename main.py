from datamatrix import DatamatrixGenerator
# Example usage
if __name__ == "__main__":
    datamatrix = DatamatrixGenerator()
    datamatrix.generate("Hello, DataMatrix", "test_datamatrix.png")
