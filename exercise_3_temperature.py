import sys


def main():
    temperature_c=float(input("temperature_in_°c:"))
    temperature_f= temperature_c * 9/5 + 32
    print(f"The temperature in °F is {temperature_f}")
    return 0


if __name__ == '__main__':
    sys.exit(main())