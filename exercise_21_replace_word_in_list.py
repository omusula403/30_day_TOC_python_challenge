import sys


def main():
    #Store words in a list
    my_list = ["Monday", "Tuesday", "Wednesday"]
    print(f"List before replacing second word is {my_list}")
    #Replace Second word in list
    my_list[1] = "Happy"
    print(f"List after replacing second word is {my_list}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
