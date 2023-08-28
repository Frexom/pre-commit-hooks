# print_arguments/main.py
import subprocess


def main():
    result = subprocess.run(["pytest", "-rf"], stdout=subprocess.PIPE)
    lines = result.stdout.decode('utf-8').split("\n")[:-1]


    if "failed" in lines[-1]:
        error_output(lines)
        exit(1)




def error_output(lines: list[str]):
    print('\033[91m')
    error_report = False
    for line in lines:
        if "FAILURE" in line:
            error_report = True

        if error_report:
            print(line)
    print('\033[0m')

if __name__ == "__main__":
    main()
