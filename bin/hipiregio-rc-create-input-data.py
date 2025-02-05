#!/usr/bin/env python3

import json
import argparse
from argparse import RawTextHelpFormatter
import logging
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s\t%(message)s')


from hipiregio.rc.rc_raw_reader import RCRawReader


def parse_arguments():
    """parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="""Creates single JSON file to be used to query given model with given reading comprehension test.

Useful use cases:
        - create all inputs for given language/dialect (in this example Polish dialect from Wielkopolska)
        ./hipiregio-rc-create-input-data.py -c pl_WLKP
        """,
        formatter_class=RawTextHelpFormatter
    )

    parser.add_argument(
        '--culture', '-c',
        required=True,
        help='Culture to process, e.g. pl_PL (canonical Polish), pl_WLKP (Polish dialect from Wielkopolska) etc.')

    parser.add_argument(
        '--output', '-o',
        required=True,
        help='Output file.')

    args = parser.parse_args()

    return args


def main():
    args = parse_arguments()

    reader = RCRawReader(culture=args.culture)

    input_data = reader.read_data()
    json_string = json.dumps(input_data.to_dict(), ensure_ascii=False, indent=4)

    print(json_string)

    print("PROMPT 0:")
    print(input_data.create_prompt_for_question(0))



main()
