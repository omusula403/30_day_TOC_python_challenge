import sys


def main():
    #prompt user to input two words
    first_word = input ("Enter First Word:")
    second_word = input ("Enter Second Word:")
    #print two words with space
    print(first_word + " " + second_word)
    return 0


if __name__ == '__main__':
    sys.exit(main())