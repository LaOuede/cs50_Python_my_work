def main():
    math = input("Expression: "). strip().split(' ')
    res = find_arg(math)
    print(f"{res:.1f}")


def find_arg(math):
    match math[1]:
        case "+":
            res = float(math[0]) + float(math[2])
        case "-":
            res = float(math[0]) - float(math[2])
        case "*":
            res = float(math[0]) * float(math[2])
        case "/":
            res = float(math[0]) / float(math[2])
    return res


main()