import sys


def main():
    #Ask user to input three words, one per input
    first_word = input("Please Enter First Word: ")
    second_word = input("Please Enter Second Word: ")
    third_word = input("Please Enter Third Word: ")
    #Store the words in a list
    my_list = ["first_word", "second_word", "third_word"]
    #Print the list exactly as python displays it
    print(my_list)
    return 0


if __name__ == '__main__':
    sys.exit(main())