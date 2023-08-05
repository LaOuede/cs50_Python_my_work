def main():
    input = input("Fraction: ").strip()
    fraction = convert(input)
    res = gauge(fraction)
    print(res)


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            num = int(x)
            den = int(y)
            res = round(num / den * 100)
            if res <= 100:
                return res
            else:
                fraction = input("Fraction: ").strip()
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
