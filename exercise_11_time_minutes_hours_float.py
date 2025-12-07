import sys


def main():
    #ask user to unput number representing minutes
    my_minutes =int (input ("Enter Number of minutes:" ))
    #convert to float (Hours)
    hours = float(my_minutes) / 60

    #print You entered X minutes which is Y hours
    print(f"You entered {my_minutes} Minutes which is {hours} hours")

    return 0


if __name__ == '__main__':
    sys.exit(main())