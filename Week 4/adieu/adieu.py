def main():
    list = []
    while True:
        try:
            x = input("Name: ").strip().title()
            list.append(x)
        except EOFError:
            print("\nAdieu, adieu, to ", end="")
            if len(list) == 1:
                print(f"{list[0]}")
            elif len(list) == 2:
                print(f"{list[0]} and {list[1]}")
            else:
                i = 0
                while i < len(list) - 1:
                    print(f"{list[i]}, ", end="")
                    i += 1
                print(f"and {list[i]}")
            return 0


main()
