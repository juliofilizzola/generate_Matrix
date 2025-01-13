# DataMatrix Generator

This project is a DataMatrix generator written in Python. It allows you to generate DataMatrix barcodes from text input and save them as image files.

## Features

- Generate DataMatrix barcodes from text input
- Save generated DataMatrix as PNG images
- Customizable output directory
- Error handling and logging

## Requirements

- Python 3.x
- `pylibdmtx`
- `Pillow`
- `pytest` (for testing)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/datamatrix-generator.git
    cd datamatrix-generator
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:
    ```sh
    python3 main.py
    ```

2. Follow the prompts to enter the file name and the message for the DataMatrix.

## Project Structure

- `core/`
  - `datamatrix.py`: Contains the `DatamatrixGenerator` class for generating DataMatrix barcodes.
  - `errors/`
    - `error_handler.py`: Contains the error handling logic.
- `input/`
  - `getTerminalInput.py`: Contains the function to get input from the terminal.
- `main.py`: Entry point of the application.
- `tests/`
  - `test_datamatrix.py`: Contains tests for the `DatamatrixGenerator` class.

## Testing

To run the tests, use the following command:
```sh
pytest