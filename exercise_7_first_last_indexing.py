import sys


def main():
    my_word = input("Enter a word: ")
    #print user word
    print(my_word)
    #print first character
    print(f"first character of {my_word} is {my_word[0]}")
    #print last character
    print(f"last character of {my_word} is {my_word[-1]}")
    return 0


if __name__ == '__main__':
    sys.exit(main())