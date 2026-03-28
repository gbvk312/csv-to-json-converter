# CSV to JSON Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, zero-dependency command-line utility for converting CSV files into formatted JSON.

## Features
- **Zero Dependencies**: Built entirely with Python's standard library.
- **Fast and Efficient**: Easily handles standard CSV files.
- **Customizable Indentation**: Format the output JSON to your exact specifications.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/gbvk312/csv-to-json-converter.git
   ```
2. Navigate into the directory:
   ```bash
   cd csv-to-json-converter
   ```
3. Make the script executable:
   ```bash
   chmod +x csv_to_json.py
   ```

## Usage
Basic usage:
```bash
./csv_to_json.py data.csv
```
This will create a file named `data.json` in the same directory.

Specify output file and indentation:
```bash
./csv_to_json.py data.csv -o output.json --indent 2
```

### Future Improvements
- Add support for detecting different CSV delimiters.
- Add support for streaming large CSV files to avoid memory issues.
