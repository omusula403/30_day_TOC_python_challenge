import sys


def main():
    #Ask User for three numbers as strings
    first_input = input ("Please Enter Your First Number:")
    second_input = input ("PLease Enter Your Second Number:")
    third_input = input ("Please Enter Your Third Number:")
    #Store the numbers in a list
    my_list = [first_input, second_input, third_input]
    #Convert list into integers using indexing
    my_list[0] = int(first_input)
    my_list[1] = int(second_input)
    my_list[2] = int(third_input)
    #Compute and Print list sum
    list_sum = sum(my_list)
    print(f"Sum of List sum is {list_sum}")
    return 0


if __name__ == '__main__':
    sys.exit(main())