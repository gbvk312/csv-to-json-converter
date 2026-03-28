#!/usr/bin/env python3
"""
Simple CLI utility to convert CSV files to JSON.
"""
import argparse
import csv
import json
import os
import sys

def convert_csv_to_json(csv_path: str, json_path: str, indent: int = 4):
    """Parses a CSV file and writes its contents to a JSON file."""
    if not os.path.isfile(csv_path):
        print(f"Error: The file '{csv_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    data = []
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=indent, ensure_ascii=False)
        print(f"Successfully converted {csv_path} to {json_path}")
    except Exception as e:
        print(f"Error writing JSON: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert a CSV file to JSON.")
    parser.add_argument("input", help="Path to the input CSV file.")
    parser.add_argument("-o", "--output", help="Path to the output JSON file. Defaults to input file with .json extension.")
    parser.add_argument("-i", "--indent", type=int, default=4, help="Indentation level for JSON (default: 4).")
    
    args = parser.parse_args()
    
    output_path = args.output
    if not output_path:
        base, _ = os.path.splitext(args.input)
        output_path = base + ".json"
        
    convert_csv_to_json(args.input, output_path, args.indent)

if __name__ == "__main__":
    main()
