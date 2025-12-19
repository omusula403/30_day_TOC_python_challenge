import sys


def main():
    #Create list of six integers
    my_list = [2,4,6,8,9,5]
    print(f"My list is {my_list}")
    #Use slicing to print middle four integers
    new_list = my_list[1:-1]
    print(f"New List after Slicing is {new_list}")

    return 0


if __name__ == '__main__':
    sys.exit(main())