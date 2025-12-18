import sys


def main():
    var_x = 10
    print(f"Original Value of x = {var_x}")

    # += assignment to variable x(addition)
    var_x +=1
    print(f"After += assignment var_x = {var_x}")

    #-= assignment to variable x (Subtraction)
    var_x = 10
    var_x -= 1
    print(f"After -= assignment var_x  = {var_x}")

    # *= assignment to variable x (Multiplication)
    var_x = 10
    var_x *= 1
    print (f"After *= assignment var_x = {var_x}")

    # **= assignment to variable x (powers)
    var_x = 10
    var_x **= 3
    print (f"After **= assignment var_x = {var_x} ")



    return 0


if __name__ == '__main__':
    sys.exit(main())