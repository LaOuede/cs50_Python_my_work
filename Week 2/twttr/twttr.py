def main():
    txt = input("Input: ").strip()
    i = 0
    lenght = len(txt)
    print(f"Output: ", end="")
    while i < lenght:
        if txt[i] == 'A' or txt[i] == 'E' or txt[i] == 'I' or txt[i] == 'O' or txt[i] == 'U' \
            or txt[i] == 'a' or txt[i] == 'e' or txt[i] == 'i' or txt[i] == 'o' or txt[i] == 'u':
            i += 1
        else:
            print(f"{txt[i]}", end="")
            i += 1
    print("")

main()