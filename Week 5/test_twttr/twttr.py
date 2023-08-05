import re


def main():
    txt = input("Input: ").strip()
    txt = shorten(txt)
    print(f"Output: {txt}")


def shorten(txt):
    txt = re.sub("[AEIOUaeiou]", "", txt)
    return txt


if __name__ == "__main__":
    main()
