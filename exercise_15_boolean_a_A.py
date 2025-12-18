import sys


def main():
    #input word
    my_word = input("Please Enter a Word: ")

    #check if word starts with 'a' or 'A'
    if my_word[0] == "a" or my_word[0] == "A":
        print(True)
        print(f"{my_word} starts with 'a' or 'A' ")
    else:
        print(False)
        print("Word does not start with 'a'")
    return 0


if __name__ == '__main__':
    sys.exit(main())