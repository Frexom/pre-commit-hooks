from __future__ import annotations

import argparse
import os
from typing import Sequence


# replacement strings
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'


def _fix_file(
        filename: str
) -> bool:
    with open(filename, mode='r') as file_processed:
        content = file_processed.read()

    fixed_content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
    with open(filename, mode='w') as file_processed:
        file_processed.write(fixed_content)

    return content != fixed_content


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    return_code = 0
    for filename in args.filenames:
        if _fix_file(filename):
            print(f"Fixing {filename}'s EOL")
            return_code = 1
    return return_code


if __name__ == '__main__':
    raise SystemExit(main())
