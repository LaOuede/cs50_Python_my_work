import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if str(sys.argv[1]).find(".py", 0, len(sys.argv[1])) == -1:
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1], "r") as file:
            src = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    nb = 0
    for line in src:
        line = line.strip()
        if len(line.strip()) > 0 and line[0] != "\n" and line[0] != "#":
            nb += 1
    print(nb)


if __name__ == "__main__":
    main()
