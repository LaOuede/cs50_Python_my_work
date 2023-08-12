import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if str(sys.argv[1]).find(".csv", 0, len(sys.argv[1])) == -1:
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1], "r") as file:
            menu = csv.reader(file)
            print(tabulate(menu, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exists")


if __name__ == "__main__":
    main()
