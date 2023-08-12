import sys
from PIL import Image, ImageOps


def main():
    parse_args()
    modify_image()


def parse_args():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if (
        (
            ".jpeg" not in sys.argv[1]
            and ".png" not in sys.argv[1]
            and ".jpg" not in sys.argv[1]
        )
    ) or (
        (
            ".jpeg" not in sys.argv[2]
            and ".png" not in sys.argv[2]
            and ".jpg" not in sys.argv[2]
        )
    ):
        sys.exit("Invalid input")
    suf1 = str(sys.argv[1]).split(".")
    suf2 = str(sys.argv[2]).split(".")
    if suf1[1] != suf2[1]:
        sys.exit("Input and output have different extensions")


def modify_image():
    try:
        before = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    after = sys.argv[2]
    size = shirt.size
    before = ImageOps.fit(before, size)
    before.paste(shirt, (0, 0), mask=shirt)
    before = before.save(after)


if __name__ == "__main__":
    main()
