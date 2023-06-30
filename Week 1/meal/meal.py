def main():
    time = input("What time is it? ")
    res = convert(time)
    if 7.0 <= res <= 8.0 :
         print("breakfast time")
    elif 12.0 <= res <= 13.0:
        print("lunch time")
    elif 18.0 <= res <= 19.0:
        print("dinner time")

def convert(time):
    time = time.split(':')
    hours = float(time[0])
    minutes = float(time[1])
    converted_time = hours + minutes / 60
    return converted_time

if __name__ == "__main__":
 main()