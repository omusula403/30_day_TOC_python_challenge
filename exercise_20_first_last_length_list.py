import sys


def main():
    #Store words in a list
    my_list = ["Monday", "Tuesday", "Wednesday"]
    #Print first word in list
    print(f"First word in list is {my_list[0]}")
    #Print last word in list
    print(f"Last Word in list is {my_list[-1]}")
    #Print length of list
    print(f"Length of list is {len(my_list)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())