def main():
    var = input("camelCase: ").strip()
    print(f"snake_case: ", end="")
    for char in var:
        if char.isupper():
            print("_", end="")
            char = char.lower()
            print(f"{char}", end="")
        else:
            print(f"{char}", end="")
    print("")


main ()