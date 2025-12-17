import sys

from pkg_resources import non_empty_lines


def main():

    #Create Variable x=None and print
    var_x = None
    print(f"Initial Variable is {var_x}")
    #Ask user for a new variable value and print
    var_x = int(input("Enter Your Variable Value: "))
    print(f"my variable is {var_x}")
    return 0


if __name__ == '__main__':
    sys.exit(main())