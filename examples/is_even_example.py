from is_even import is_even as ie

def main(number):
    if ie.is_even(number) == True:
        print("Your number is even!")
    else:
        print("You number is not even.")


if __name__ == "__main__":
    main(8)
