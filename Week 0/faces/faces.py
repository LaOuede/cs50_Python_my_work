txt = input()

i = 0
while i < len(txt):
    if txt[i] == ':' and txt[i + 1] == ')':
        print('🙂', end="")
        i += 2
    elif txt[i] == ':' and txt[i + 1] == '(':
        print('🙁', end="")
        i += 2
    else:
        print(txt[i], end="")
        i += 1
