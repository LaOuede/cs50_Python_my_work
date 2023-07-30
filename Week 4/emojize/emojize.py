import emoji

str = input("Input: ").strip()
res = emoji.emojize(str)
print(f"Output: {res}")