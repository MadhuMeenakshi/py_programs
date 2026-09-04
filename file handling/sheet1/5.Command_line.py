import sys


def filter_logs(filename, search_term):
    try:
        with open(filename, "r") as file:
            for line in file:
                if search_term in line:
                    print(line.strip())

    except FileNotFoundError:
        print("File not found.")


if len(sys.argv) != 3:
    print("Usage: python script.py <filename> <search_term>")
    sys.exit(1)

filename = sys.argv[1]
search_term = sys.argv[2]

filter_logs(filename, search_term)