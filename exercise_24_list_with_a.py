import sys


def main():
    #Ask for five words and store them in a list
    my_words = input("Please Enter five words:")
    my_list = my_words.split()
    #Print new list with words starting with 'a' or 'A' using indexing
    #if words are not equal to five print an error
    if len(my_list) == 5:
        new_list = [word for word in my_list if word[0] == "a" or word[0] == "A"]
        print(f"New List = {new_list}")
    else:
        print(f"Error: Expected 5 words, but you entered {len(my_list)}.")
    return 0


if __name__ == '__main__':
    sys.exit(main())