#!/usr/bin/env python3

import argparse
import logging
import xml.etree.ElementTree as ET

from pathlib import Path

namespace = {'tt': 'http://www.w3.org/ns/ttml'}


def check_path(argument):
    if argument is None:
        path = Path.cwd()
    else:
        path = Path(argument)

    if path.is_dir():
        return path
    else:
        logger.error('Specified path does not exist: %s', path)
        sys.exit(1)


def convert_to_srt(content):
    output = ""

    root = ET.fromstring(content)
    body = root.find('tt:body', namespace)
    div = body.find('tt:div', namespace)

    i = 1
    for entry in div.findall('tt:p', namespace):
        start_time = entry.attrib['begin'].replace('.', ',')
        end_time = entry.attrib['end'].replace('.', ',')
        text = "\n".join(entry.itertext())

        output += "{}\n{} --> {}\n{}\n\n".format(i, start_time, end_time, text)
        i += 1

    return output
    

def main():
    logging.basicConfig(format='%(asctime)-15s - %(levelname)-8s - %(message)s')
    logger = logging.getLogger('amazon-to-srt')
    logger.setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input directory', nargs='?')
    parser.add_argument('output', help='path to the output directory', nargs='?')
    args = parser.parse_args()

    input_path = check_path(args.input)
    output_path = check_path(args.output)

    valid_extensions = ['.xml', '.dfxp']

    input_files = [x for x in input_path.iterdir() if x.suffix in valid_extensions]
    for file in input_files:
        output_file = output_path / file.with_suffix('.srt').name

        try:
            convert = convert_to_srt(file.read_text(encoding='utf-8'))
            output_file.write_text(convert)
            logger.info('Converted %s to .srt format', file.name)
        except ET.ParseError:
            logger.error('The XML in %s appears to be invalid', file.name)


if __name__ == '__main__':
    main()