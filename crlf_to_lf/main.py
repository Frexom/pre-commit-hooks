import argparse
from typing import Sequence


# replacement strings
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'


def _fix_file(
        filename: str,
        keep_crlf: bool
) -> bool:
    with open(filename, mode='rb') as file_processed:
        content = file_processed.read()

    if not keep_crlf:
        fixed_content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
    else:
        fixed_content = content.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)

    with open(filename, mode='wb') as file_processed:
        file_processed.write(fixed_content)

    return content != fixed_content


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument('--keep-crlf', action='store_true')
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    return_code = 0
    for filename in args.filenames:
        if _fix_file(filename, args.keep_crlf):
            print(f"Fixing {filename}'s EOL...")
            return_code = 1
    return return_code

if __name__ == "__main__":
    main()