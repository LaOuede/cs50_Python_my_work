import sys
import csv

names = []

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if str(sys.argv[1]).find(".csv", 0, len(sys.argv[1])) == -1:
        sys.exit(f"Could not read {sys.argv[1]}")
    if  str(sys.argv[2]).find(".csv", 0, len(sys.argv[2])) == -1:
        sys.exit(f"Could not read {sys.argv[2]}")

    try:
        with open("after.csv", "a") as output:
            fieldnames = ['first name', 'last name', 'house']
            writer = csv.DictWriter(output,  fieldnames=fieldnames)
            writer.writeheader()

        with open("before.csv", "r") as input:
            content = csv.DictReader(input)
            names = list(content)
            for row in names:
                first_name, last_name = row['name'].split(',')
                first_name = first_name.strip()
                last_name = last_name.strip()
                house = row['house']
                with open("after.csv", "a") as output:
                    fieldnames = ['first', 'last', 'house']
                    writer = csv.DictWriter(output,  fieldnames=fieldnames)
                    writer.writerow({'first': first_name, 'last': last_name, 'house': house})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()