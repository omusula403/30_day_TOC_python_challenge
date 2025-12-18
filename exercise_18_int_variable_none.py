import sys


def main():
    #Ask User for a number
    user_input = input("Enter Your Number:")
    #Convert to integer
    user_int = int(user_input)
    print(f"user integer = {user_int}")
    #Reassign the Variable to None
    user_input = None
    print(f"New State of user input = {user_input}")
    return 0

#Why a Variable can change type
#Python is a dynamically typed language
#Meaning that a variable in Python does not have a fixed type upon its declaration




if __name__ == '__main__':
    sys.exit(main())