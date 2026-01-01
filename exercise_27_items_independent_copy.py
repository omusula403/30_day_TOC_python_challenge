import sys


def main():
    #Original items
    original_items = [10,20,30]
    #Create independent copy from original
    independent_copy = original_items [:]
    #print both lists
    print(f"Original Items = {original_items}")
    print(f"Independent Copy = {independent_copy}")
    return 0


if __name__ == '__main__':
    sys.exit(main())