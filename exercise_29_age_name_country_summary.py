import sys


def main():

    #Ask User for name, age and country
    user_name = input("Enter Your Name:")
    user_age = int (input("Enter Your Age:"))
    user_country = input("Enter Your Country:")

    #Store results in a list
    user_profile = [user_name, user_age, user_country]

    #Produce new list from initial list
    #Print name of user in uppercase
    #Add 5 to age of user
    #Print country of user in lowercase
    user_summary = [user_profile[0].upper(), user_profile[1] + 5, user_profile[2].lower()]

    #Print both lists
    print(f"Original List = {user_profile}")
    print(f"New List = {user_summary}")
    return 0


if __name__ == '__main__':
    sys.exit(main())