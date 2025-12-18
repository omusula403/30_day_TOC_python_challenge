import sys


def main():
    #prompt user to input integer
    my_integer = input ("Enter Your Integer:")
    #convert integer to float
    my_float = float(my_integer)
    #print integer and float values
    print(f"my integer is : {my_integer}")
    print(f"my float is : {my_float}")
    return 0


if __name__ == '__main__':
    sys.exit(main())