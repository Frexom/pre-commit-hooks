import subprocess
import re


def main():
    root = subprocess.run(["git", "rev-parse", "--show-toplevel"], stdout = subprocess.PIPE)
    root = root.stdout.decode("utf-8")[:-1]

    result = subprocess.run(["pytest", "-rf", root], stdout=subprocess.PIPE)
    lines = result.stdout.decode('utf-8').split("\n")[:-1]


    if "failed" in lines[-1] or "error" in lines[-1]:
        error_output(lines)
        exit(1)


def error_output(lines: list[str]):
    print('\033[91m')
    error_report = False
    for line in lines:
        if re.match("^==* FAILURES ==*", line) or re.match("^==* ERRORS ==*", line):
            error_report = True

        if error_report:
            print(line)
    print('\033[0m')

if __name__ == "__main__":
    main()
