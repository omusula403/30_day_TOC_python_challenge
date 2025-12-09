import sys


def main():
    try:
        #input int a and b
        int_a = int(input("Enter The First Number:"))
        int_b = int (input("Enter The Second Number:"))
        #check if int_a is greater than int_b
        if int_a > int_b:
            print("True")
        else:
            print("False")
        # check if int_a is equal to int_b
        if int_a == int_b:
            print("True")
        else:
            print("False")
        # check if int_a is not equal to int_b
        if int_a != int_b:
            print("True")
        else:
            print("False")
        return 0
    except ValueError:
        print("Please Enter a Number")



if __name__ == '__main__':
    sys.exit(main())