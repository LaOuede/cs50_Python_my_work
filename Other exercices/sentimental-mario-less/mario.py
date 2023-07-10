from cs50 import get_int

height = -1

# print the question as long as x is not within the range 1 to 8
while (height < 1 or height > 8):
    height = get_int("Height: ")


# Upgrade
for i in range(height):
    print ("#" * (i + 1))

""" #First implementation
y = height
while y > 0:
    x = 0
    while x < y - 1:
        print(" ", end="")  # print spaces
        x += 1
    z = y
    while z <= height:
        print("#", end="")  # print bricks
        z += 1
    print("")  # print new line
    y -= 1 """
