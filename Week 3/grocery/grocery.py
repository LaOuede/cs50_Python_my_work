def main():
    grocery = {
        "APPLE": 0,
        "TOMATO": 0,
        "MANGO": 0,
        "STRAWBERRY": 0,
        "SWEET POTATO": 0,
        "TORTILLA": 0,
        "BANANA": 0,
        "SUGAR": 0
    }
    while True:
        try:
            item = input().strip().upper()
            if item in grocery:
                grocery[item] += 1
        except ValueError:
            pass
        except EOFError:
            print ("\n", end="")
            for i in grocery:
                if grocery[i] > 0:
                    print (f"{grocery[i]} {i}")
            return 0


main ()