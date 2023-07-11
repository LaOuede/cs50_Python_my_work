def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            date = input("Date: ").strip()
            if date.find('/') > 0:
                date = date.split('/')
                day = int(date[1])
                month = int(date[0])
                if 0 < day <= 31 and 0 < month <= 12:
                    year = int(date[2])
                    print(f"{year}-{month:02}-{day:02}")
                    return (0)
            else:
                if date.find(',') > 0:
                    date = date.split(' ')
                    day = int(date[1].removesuffix(','))
                    if 0 < day <= 31:
                        month = 1
                        for i in months:
                            if date[0] == i:
                                break
                            month += 1
                        year = int(date[2])
                        print(f"{year}-{month:02}-{day:02}")
                        return (0)
        except ValueError:
            pass


main ()