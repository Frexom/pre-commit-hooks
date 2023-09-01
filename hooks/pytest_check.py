import argparse
import os
import re
import subprocess
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument("--run-only", nargs="*", help="The files/folders to run.")
    args = parser.parse_args(argv)

    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    repo_root = result.stdout.decode("utf-8")[:-1]

    if result.returncode != 0:
        print(result.stderr.decode("utf-8"))
        exit(1)

    # Going to repo's root
    original_path = os.getcwd()
    os.chdir(repo_root)

    # Running the pytest command
    result = subprocess.run(["pytest"] + (args.run_only or []), stdout=subprocess.PIPE)
    lines = result.stdout.decode("utf-8").split("\n")[:-1]

    # Going back to the original path
    os.chdir(original_path)

    if result.returncode == 0:
        exit(0)

    if "failed" in lines[-1] or "error" in lines[-1]:
        error_output(lines)
        exit(1)

    exit(1)


def error_output(lines: list[str]):
    print("\033[91m")
    error_report = False
    for line in lines:
        if re.match("^==* FAILURES ==*", line) or re.match("^==* ERRORS ==*", line):
            error_report = True

        if error_report:
            pass
            print(line)
    print("\033[0m")


if __name__ == "__main__":
    main()
