def main():
    try:
        txt = input("Fraction: ").strip().split('/')
        x = int(txt[0])
        y = int(txt[1])
        if y > 0 and x <= y:
            res = round(x / y * 100)
            if 0 <= res <= 1:
                print ("E")
            elif 100 >= res >= 99:
                print ("F")
            else:
                print (f"{res}%")
        else:
            txt = input("Fraction: ").strip().split('/')

        txt = input("Fraction: ").strip().split('/')


main()