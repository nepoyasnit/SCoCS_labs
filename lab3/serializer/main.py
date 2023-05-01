import argparse
from src.controller import Controller
from src.constants import SAME_TYPE_ERROR


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Serializer of JSON, YAML, TOML')
    parser.add_argument('input_dir', type=str, help='Input directory')
    parser.add_argument('source_format', type=str, help='Format(JSON, YAML, TOML) of source')
    parser.add_argument('result_format', type=str, help='Format(JSON, YAML, TOML) for result')
    parser.add_argument('output_dir', type=str, help='Output directory')
    arguments = parser.parse_args()

    result_format = arguments.result_format
    source_format = arguments.source_format

    if source_format == result_format:
        print(SAME_TYPE_ERROR)

    source_serializer = Controller(source_format)
    result_serializer = Controller(result_format)

    with open(arguments.input_dir) as file:
        obj = source_serializer.load(file)
        with open(arguments.output_dir) as output_file:
            result_serializer.serializer.dump(obj, output_file)

