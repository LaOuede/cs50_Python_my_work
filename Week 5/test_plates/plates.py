def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if valid_lenght(s) :
        if valid_char(s):
            if valid_letters(s):
                if valid_numbers(s):
                    return True
    else:
        return False


def valid_lenght(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


def valid_char(s):
    if s.isalnum() :
        return True
    else:
        return False


def valid_letters(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False


def valid_numbers(s):
    i = 1
    while i < (len(s) / 2):
        if s[i].isdigit():
            return False
        i += 1
    if s[i] == '0':
        return False
    return True


if __name__ == "__main__":
    main()

"""
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable …
    vanity plate; AAA22A would not be acceptable. The first number used cannot be a 0.”
“No periods, spaces, or punctuation marks are allowed.”
"""