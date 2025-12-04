import sys


def main():
    #prompt user to input message
    my_message = input ("Enter Your Message: ")
    #print user message three times
    print((my_message + "\n") * 3)
    return 0


if __name__ == '__main__':
    sys.exit(main())