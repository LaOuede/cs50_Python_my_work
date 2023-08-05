def main():
    text = input("Greeting: ").strip().capitalize()
    print(f"${value(text)}")


def value(text):
    if text.split()[0] == "Hello" or text.split()[0] == "Hello,":
        return 0
    elif text.split()[0] != "Hello" and text[0] == "H":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
