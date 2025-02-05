# MIDI Converter App

This project is a Python application designed to convert MIDI files from EZ Drummer 3 format to the PV edition format. It follows the SOLID principles and employs a Test-Driven Development (TDD) approach.

## Project Structure

```
midi-converter-app
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── converters
│   │   ├── __init__.py
│   │   └── midi_converter.py
│   ├── models
│   │   ├── __init__.py
│   │   └── midi_file.py
│   ├── services
│   │   ├── __init__.py
│   │   └── conversion_service.py
│   └── utils
│       ├── __init__.py
│       └── file_utils.py
├── tests
│   ├── __init__.py
│   ├── test_midi_converter.py
│   ├── test_conversion_service.py
│   └── test_file_utils.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/midi-converter-app.git
   ```
2. Navigate to the project directory:
   ```
   cd midi-converter-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Testing

To run the tests, use:
```
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.