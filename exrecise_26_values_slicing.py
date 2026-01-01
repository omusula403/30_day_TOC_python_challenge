import sys


def main():
    #Store values
    values = [5,6,7,8]
    #Print first two(index 0 and 1) using slicing; slice from beginning up to but not including index 2
    first_two = values[:2]
    print(first_two)
    return 0


if __name__ == '__main__':
    sys.exit(main())