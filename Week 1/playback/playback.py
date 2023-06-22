text = input()
for i in text:
    if i == ' ':
        print('...', end="")
    else:
        print(i, end="")
print('\n')