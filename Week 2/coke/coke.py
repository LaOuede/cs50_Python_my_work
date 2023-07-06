def main():
    due = 50
    print(f"Amount Due: {due}")
    while due > 0:
        txt = input("Insert coin: ").strip()
        coin = int(txt)
        if coin == 25 or coin == 10 or coin == 5:
            due -= coin
            if due > 0:
                print(f"Amount Due: {due}")
            elif due == 0:
                print(f"Change Owed: {due}")
            elif due < 0:
                print(f"Change Owed: {-due}")
        else:
            print(f"Amount Due: {due}")

main()