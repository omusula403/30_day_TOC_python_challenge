import sys


def main():
    try:
        #input age
        my_age = int(input("Enter Your Age: "))

        #check if age is true or false
        if my_age >= 18:
            print("True")
        else:
            print("False")
        return 0
    except ValueError:
        print("Enter a Valid Age!")

if __name__ == '__main__':
    sys.exit(main())