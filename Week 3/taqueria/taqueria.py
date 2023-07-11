def main():
    res = 0
    while True:
        try:
            x = input("Item: ").strip().title()
            menu = {
                "Baja Taco": 4.00,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
            }
            if x in menu:
                res += menu[x]
                print(f"Total: ${res:.2f}")
        except ValueError:
            x = input("Item: ").title()
        except EOFError:
            return 0


main()
