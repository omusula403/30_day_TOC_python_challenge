import sys


def main():
    try:
        #input user word
        my_word= input("Enter Your Word:")
        #input a number
        my_number = int(input("Enter Your Number: "))
        #repeat word number times
        print((my_word + "\n" )* my_number)

        return 0
    except ValueError:
        print("Invalid Input")

if __name__ == '__main__':
    sys.exit(main())
