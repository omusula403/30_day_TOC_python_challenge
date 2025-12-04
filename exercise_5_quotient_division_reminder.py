import sys


def main():
    interger_1=int(input ("Enter a Number: "))
    interger_2=int(input("Enter another Number:"))
    print (f"quotient = {interger_1/interger_2}")
    print (f"divisor = {interger_1//interger_2}")
    print (f"remainder = {interger_1%interger_2}")
    return 0


if __name__ == '__main__':
    sys.exit(main())