import emoji
def convert(x):
    if x == emoji.emojize(x):
        return emoji.emojize(x, language = 'alias')
    else:
        return emoji.emojize(x)
def main():
    x = input("Input: ")
    y = convert(x)
    print(f"Output: {y}")

if __name__ == "__main__":
    main()
