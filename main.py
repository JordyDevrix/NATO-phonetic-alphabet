from nato_lib import nato_alpabet


def main():
    while True:
        word = list(input("enter string: "))
        for letter in range(len(word)):
            print(nato_alpabet[word[letter]])


if __name__ == '__main__':
    main()
