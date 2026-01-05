import sys


def main():
    #Ask User for Four integers
    user_input = input("Please enter four integers:")
    #Store the four integers in nums
    nums = list(map(int, user_input.split()))


    if len(nums) == 4:
        #Replace first number in list with its square
        nums[0] = nums[0]**2
        #Replace last number in list with its cube
        nums[-1] = nums[-1]**3
        #Compute and print the sum of four numbers in list
        nums_sum = sum(nums)
        print(f"New list = {nums}")
        print(f"sum = {nums_sum}")
    else:
        print(f"Error: Expected 4 integers, but you entered {len(nums)}.")


    return 0


if __name__ == '__main__':
    sys.exit(main())
